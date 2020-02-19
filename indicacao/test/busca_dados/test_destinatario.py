from django.test import TestCase
from indicacao.busca_dados.destinatario import Destinatario


class DestinatarioTest(TestCase):
    def test_identificar_autor_anterior_2020(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '
        destinatario = Destinatario().recuperar(dados)
        self.assertEqual('SECRETARIA DE URBANISMO', destinatario)

    def test_identificar_autor_2020(self):
        dados = """Nº 1 Ano 2020 Autor: Anderson Ferreira da Silva Destinatário: Secretaria Municipal de Saúde Assunto: Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde."""

        destinatario = Destinatario().recuperar(dados)
        self.assertEqual('SECRETARIA MUNICIPAL DE SAUDE', destinatario)
