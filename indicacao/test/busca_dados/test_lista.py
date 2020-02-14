from django.test import TestCase
from indicacao.busca_dados.lista import Lista


class ListaTest(TestCase):
    def setUp(self):
        self.__conteudo = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""
        self.__conteudo = self.__conteudo.lstrip()

    def test_recuperar_dados_lista(self):
        dados = Lista().recuperar(self.__conteudo)
        esperado = ['  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    ']
        self.assertEqual(esperado, dados)
