from django.test import TestCase
from indicacao.busca_dados.numero import Numero


class NumeroTest(TestCase):
    def test_recuperar_numero_anterior_2020(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '
        numero = Numero().recuperar(dados)
        self.assertEqual(222, numero)

    def test_recuperar_numero_ano_2020(self):
        dados = ' Nº 1 Ano 2020 Autor: Anderson Ferreira da Silva Destinatário: Secretaria Municipal de Saúde Assunto: Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde.'
        numero = Numero().recuperar(dados)
        self.assertEqual(1, numero)

    def test_recuperar_numero_ano_2020_com_barra(self):
        dados = ' nº 18/2020 Autor: Anderson Ferreira da Silva Destinatário: Secretaria Municipal de Saúde Assunto: Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde.'
        numero = Numero().recuperar(dados)
        self.assertEqual(18, numero)
