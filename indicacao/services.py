import re

from django.db import IntegrityError
from django.db.models import Q
from tika import parser
from lib.util.string import normalize

from pauta.models import Pauta
from vereador.models import Vereador
from executor.models import Executor
from .models import Indicacao
from .busca_dados.lista import Lista
from .busca_dados.numero import Numero
from .busca_dados.autor import Autor
from .busca_dados.destinatario import Destinatario
from .busca_dados.assunto import Assunto


class IndicacaoServices:
    def __init__(self, *args, **kwargs):
        self.__pauta = None
        return super().__init__(*args, **kwargs)

    def buscar_indicacoes(self):
        pautas = Pauta.objects.all().filter(indicacao_exportada=False)
        for pauta in pautas:
            try:
                self.__pauta = pauta
                self.__buscar_dados()
                self.__set_indicacoes_exportadas()
            except IntegrityError:
                print('Algum erro')

    def __set_indicacoes_exportadas(self):
        self.__pauta.indicacao_exportada = True
        self.__pauta.save()

    def __buscar_dados(self):
        pauta = self.__pauta
        content = self.__recuperar_conteudo(pauta.link)
        matches = self.__recuperar_dados_lista(content)

        if matches is None:
            return

        for match in matches:
            numero = self.__indicacao_numero(match)
            if not self.__numero_valido(numero):
                continue

            if self.__numero_ja_cadastrado(numero, pauta):
                continue

            assunto = self.__indicacao_assunto(match)
            autor = self.__indicacao_autor(match)
            vereador = self.__buscar_vereador(autor)
            destinatario = self.__criar_buscar_executor(
                self.__indicacao_destinatario(match)
            )

            self.__salvar_indicacao(
                pauta=pauta,
                vereador=vereador,
                destinatario=destinatario,
                numero=numero,
                assunto=assunto
            )

    def __recuperar_conteudo(self, link):
        raw = parser.from_file(link)
        return normalize(raw['content'])

    def __numero_valido(self, numero):
        if numero is None:
            return False
        return True

    def __numero_ja_cadastrado(self, numero, pauta):
        numero_cadastrado = Indicacao.objects.filter(
            Q(numero=numero) & Q(pauta=pauta)
        )

        if numero_cadastrado:
            return True
        return False

    def __buscar_vereador(self, nome):
        return Vereador.objects.buscar_nome(nome)

    def __criar_buscar_executor(self, nome):
        obj, created = Executor.objects.get_or_create(
            nome=nome
        )
        return obj

    def __salvar_indicacao(self, **dados):
        indicacao = Indicacao(
            pauta=dados['pauta'],
            vereador=dados['vereador'],
            destinatario=dados['destinatario'],
            numero=dados['numero'],
            assunto=dados['assunto']
        )
        indicacao.save()

    def __recuperar_dados_lista(self, content):
        return Lista().recuperar(content)

    def __indicacao_numero(self, indicacao):
        return Numero().recuperar(indicacao)

    def __indicacao_autor(self, indicacao):
        return Autor().recuperar(indicacao)

    def __indicacao_destinatario(self, indicacao):
        return Destinatario().recuperar(indicacao)

    def __indicacao_assunto(self, indicacao):
        return Assunto().recuperar(indicacao)
