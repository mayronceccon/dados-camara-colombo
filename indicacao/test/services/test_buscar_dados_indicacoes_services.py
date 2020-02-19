import os
from datetime import date
from django.test import TestCase
from unittest.mock import Mock
from lib.parser.tika import Tika
from indicacao.services.buscar_dados_indicacoes_services \
    import BuscarDadosIndicacoesServices
from vereador.models import Vereador
from executor.models import Executor
from pauta.models import Pauta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BuscarDadosIndicacoesServicesTest(TestCase):
    def test_set_pauta(self):
        parser = Mock(spec=Tika)
        b = BuscarDadosIndicacoesServices(parser)

        with self.assertRaises(TypeError):
            b.buscar_dados("")

    def test_retorno_esperado(self):
        arquivo_texto_esperado = "%s/services/texto_parser.txt" % (BASE_DIR)
        with open(arquivo_texto_esperado, 'r') as f:
            texto_esperado = f.read()

        parser_mock = Mock(spec=Tika)
        parser_mock.get_text = Mock(return_value=texto_esperado)

        buscar_indicacoes = BuscarDadosIndicacoesServices(parser_mock)

        pauta = Pauta(
            descricao="Descrição da Pauta",
            link="https://google.com",
            data_sessao=date.today()
        )
        pauta.save()

        # Indicação 1
        vereador_prego = Vereador(
            nome="Anderson Ferreira da Silva",
            apelido="Anderson Prego"
        )
        vereador_prego.save()

        executor_sec_saude = Executor(
            nome="Secretaria Municipal de Saúde"
        )
        executor_sec_saude.save()

        # Indicação 2
        vereador_vagner = Vereador(
            nome="Vagner Brandão",
            apelido="Vagner da Viação"
        )
        vereador_vagner.save()

        executor_humberto = Executor(
            nome="Senhor Humberto Scheleder Encarregado do tráfego Coordenação da Região Metropolitana de Curitiba-COMEC Rodovia Da Uva,nº 3884-Roça Grande Colombo/PR"
        )
        executor_humberto.save()

        # Indicação 3
        vereador_marquinho = Vereador(
            nome="João Marcos Berlesi",
            apelido="Marquinho Berlesi"
        )
        vereador_marquinho.save()

        executor_sec_gov = Executor(
            nome="Secretaria de Governo"
        )
        executor_sec_gov.save()

        valores = buscar_indicacoes.buscar_dados(pauta)

        esperado = [
            {
                'pauta': pauta,
                'vereador': vereador_prego,
                'destinatario': executor_sec_saude,
                'numero': 1,
                'assunto': "Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde."
            },
            {
                'pauta': pauta,
                'vereador': vereador_vagner,
                'destinatario': executor_humberto,
                'numero': 2,
                'assunto': "Solicito ao setor competente a adição de uma linha de ônibus que passe no Centro De Especialidades Médicas do Jd Osasco e que venha ter integração com o terminal do Roça Grande em Colombo/PR."
            },
            {
                'pauta': pauta,
                'vereador': vereador_marquinho,
                'destinatario': executor_sec_gov,
                'numero': 3,
                'assunto': "Viabilize, junto às secretarias e departamentos competentes, novos estudos para reimplantação de seis lombadas e a implantação de quatro novas, conforme sugestões indicadas abaixo, para a rua Presidente Faria, localizada no bairro Colônia Faria. 1° Rua Presidente Faria n°5255, próximo à entrada principal da empresa Eternit - já existia 2° Rua Presidente Faria n°4701, próximo à entrada da Associação Paranaense do Ministério Público - já existia 3° Trecho que dá acesso ao Município de Campina Grande do Sul, próximo ao ponto de ônibus e da Antiga serraria Ferrarini - já existia 4° Trecho que dá acesso ao Município de Campina Grande do Sul, próximo de uma placa de sinalização indicativa de limite entre e municípios de Campina Grande do Sul e Colombo - já existia 5° Rua Presidente Faria n°4369, próximo à entrada do Centro de Treinamento do Capitão – nova 6° Rua Presidente Faria próximo do n°4039 – nova 7° Rua Presidente Farias n°3715, próximo ao alinhamento do poste residencial de energia - já existia 8° Rua Presidente Faria n°2480 – nova 9° Rua Presidente Faria n°2262 – nova 10° Rua Presidente Faria n°1544 - já existia"
            },
        ]

        self.assertCountEqual(esperado, valores)

    def test_sem_informacoes_na_lista(self):
        texto_esperado = ""
        parser_mock = Mock(spec=Tika)
        parser_mock.get_text = Mock(return_value=texto_esperado)

        buscar_indicacoes = BuscarDadosIndicacoesServices(parser_mock)

        pauta = Pauta(
            descricao="Descrição da Pauta",
            link="https://google.com",
            data_sessao=date.today()
        )
        pauta.save()

        valores = buscar_indicacoes.buscar_dados(pauta)

        self.assertEqual([], valores)
