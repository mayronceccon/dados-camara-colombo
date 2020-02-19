from vereador.models import Vereador
from executor.models import Executor
from indicacao.busca_dados.lista import Lista
from indicacao.busca_dados.numero import Numero
from indicacao.busca_dados.autor import Autor
from indicacao.busca_dados.destinatario import Destinatario
from indicacao.busca_dados.assunto import Assunto
from pauta.models import Pauta


class BuscarDadosIndicacoesServices:
    def __init__(self, parser):
        self.__parser = parser

    def buscar_dados(self, pauta):
        if not isinstance(pauta, Pauta):
            raise TypeError()

        self.__pauta = pauta
        content = self.__recuperar_conteudo(self.__pauta.link)
        matches = self.__recuperar_dados_lista(content)

        if not matches:
            return []

        self.__indicacoes = []

        for match in matches:
            try:
                numero = self.__indicacao_numero(match)
                assunto = self.__indicacao_assunto(match)
                autor = self.__indicacao_autor(match)
                vereador = self.__buscar_vereador(autor)
                destinatario = self.__criar_buscar_executor(
                    self.__indicacao_destinatario(match)
                )

                self.__indicacoes.append({
                    'pauta': self.__pauta,
                    'vereador': vereador,
                    'destinatario': destinatario,
                    'numero': numero,
                    'assunto': assunto
                })
            except Exception:
                continue
        return self.__indicacoes

    def __recuperar_conteudo(self, link):
        self.__parser.set_link(link)
        return self.__parser.get_text()

    def __buscar_vereador(self, nome):
        return Vereador.objects.buscar_nome(nome)

    def __criar_buscar_executor(self, nome):
        obj, created = Executor.objects.get_or_create(
            nome=nome
        )
        return obj

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
