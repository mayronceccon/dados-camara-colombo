import re

from django.db import IntegrityError
from django.db.models import Q
from tika import parser

from lib.util.string import sanitize
from pauta.models import Pauta
from vereador.models import Vereador
from executor.models import Executor

from .models import Indicacao


class IndicacaoServices:
    _pauta = None

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def buscar_indicacoes(self):
        pautas = Pauta.objects.all().filter(indicacao_exportada=False)
        for pauta in pautas:
            try:
                self._pauta = pauta
                self.buscar_dados()
                self._set_indicacoes_exportadas()
            except IntegrityError:
                print('Algum erro')

    def _set_indicacoes_exportadas(self):
        self._pauta.indicacao_exportada = True
        self._pauta.save()

    def buscar_dados(self):
        pauta = self._pauta
        content = self._recuperar_conteudo(pauta.link)
        matches = self._recuperar_dados_lista(content)

        if matches is None:
            return

        for match in matches:
            numero = self._indicacao_numero(match)
            if not self._numero_valido(numero):
                continue

            if self._numero_ja_cadastrado(numero, pauta):
                continue

            assunto = self._indicacao_assunto(match)
            autor = self._indicacao_autor(match)
            vereador = self._buscar_vereador(autor)
            destinatario = self._criar_buscar_executor(
                self._indicacao_destinatario(match)
            )

            self._salvar_indicacao(
                pauta=pauta,
                vereador=vereador,
                destinatario=destinatario,
                numero=numero,
                assunto=assunto
            )

    def _recuperar_conteudo(self, link):
        raw = parser.from_file(link)
        conteudo = self._limpar_conteudo(raw['content'])
        return conteudo

    def _limpar_conteudo(self, conteudo):
        conteudo = conteudo.strip().rstrip('\r\n').replace(
            "\n", "").replace("\r", "").replace("  ", " ")
        conteudo = conteudo.strip().rstrip('\r\n').replace(
            "\n", "").replace("\r", "").replace("  ", " ")
        return conteudo

    def _numero_valido(self, numero):
        if numero is None:
            return False
        return True

    def _numero_ja_cadastrado(self, numero, pauta):
        numero_cadastrado = Indicacao.objects.filter(
            Q(numero=numero) & Q(pauta=pauta)
        )

        if numero_cadastrado:
            return True
        return False

    def _buscar_vereador(self, nome):
        return Vereador.objects.buscar_nome(nome)

    def _criar_buscar_executor(self, nome):
        obj, created = Executor.objects.get_or_create(
            nome=nome
        )
        return obj

    def _salvar_indicacao(self, **dados):
        indicacao = Indicacao(
            pauta=dados['pauta'],
            vereador=dados['vereador'],
            destinatario=dados['destinatario'],
            numero=dados['numero'],
            assunto=dados['assunto']
        )
        indicacao.save()

    def _recuperar_dados_lista(self, content):
        regex = r"(?:cação\s)(.*?)(?:\sIndi|\sColombo, [0-9]{1,2} de|\sTribuna Livre)"
        return re.findall(regex, content)

    def _indicacao_numero(self, indicacao):
        regex = r"((?:N°[:]?[\s]?)([0-9]{1,})((?:\s{0,}Autor|Autora)))"
        matches = re.search(regex, indicacao.lstrip())
        if matches is not None:
            return int(matches.group(2))

    def _indicacao_autor(self, indicacao):
        regex = r"((?:Autor[a]{0,}[:]?\s{0,})(.*?)(?:\s{0,}Destinatário))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            autor = matches.group(2).split("(")[0].strip().lstrip()
            return self._limpar_conteudo(autor)

    def _indicacao_destinatario(self, indicacao):
        regex = r"((?:Destinatário[:]?\s)(.*?)(?:\sAssunto:))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            destinatario = sanitize(matches.group(2)).upper()
            return self._limpar_conteudo(destinatario)

    def _indicacao_assunto(self, indicacao):
        regex = r"((?:Assunto[:]?\s)(.*))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            assunto = matches.group(2).lstrip()
            return self._limpar_conteudo(assunto)
