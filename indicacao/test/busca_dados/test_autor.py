from django.test import TestCase
from indicacao.busca_dados.autor import Autor


class AutorTest(TestCase):
    def setUp(self):
        self.__dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

    def test_identificar_autor(self):
        autor = Autor().recuperar(self.__dados)
        self.assertEqual('Renato Lunardon', autor)
