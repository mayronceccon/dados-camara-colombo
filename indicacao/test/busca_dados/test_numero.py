from django.test import TestCase
from indicacao.busca_dados.numero import Numero


class NumeroTest(TestCase):
    def setUp(self):
        self.__dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

    def test_recuperar_numero(self):
        numero = Numero().recuperar(self.__dados)
        self.assertEqual(222, numero)
