import re
from django.db import IntegrityError
from tika import parser
from lib.parser.tika import Tika
from pauta.models import Pauta
from .models import Indicacao
from .services.buscar_dados_indicacoes_services \
    import BuscarDadosIndicacoesServices


class IndicacaoPautaServices:
    def __init__(self):
        tk = Tika(parser)

        self.__indi = BuscarDadosIndicacoesServices(tk)
        self.__salvar = IndicacaoSalvarServices()
        super().__init__()

    def buscar(self):
        pautas = Pauta.objects.all().filter(indicacao_exportada=False)
        for pauta in pautas:
            try:
                indicacao = self.__indi.buscar_dados(pauta)
                self.__salvar.salvar_indicacao(indicacao)
                self.__set_indicacoes_exportadas(pauta)
            except Exception:
                continue

    def __set_indicacoes_exportadas(self, pauta):
        pauta.indicacao_exportada = True
        pauta.save()


class IndicacaoSalvarServices:
    def __init__(self):
        super().__init__()

    def salvar_indicacao(self, d):
        for dados in d:
            indicacao = Indicacao(
                pauta=dados['pauta'],
                vereador=dados['vereador'],
                destinatario=dados['destinatario'],
                numero=dados['numero'],
                assunto=dados['assunto']
            )
            indicacao.save()

