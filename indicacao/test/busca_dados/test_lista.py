from django.test import TestCase
from indicacao.busca_dados.lista import Lista


class ListaTest(TestCase):
    def test_recuperar_dados_lista_anterior_2020(self):
        conteudo = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""
        dados = Lista().recuperar(conteudo)

        esperado = ['  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    ']

        self.assertEqual(esperado, dados)

    def test_recuperar_dados_lista_2020(self):
        conteudo = """Indicação Nº 1 Ano 2020 Autor: Anderson Ferreira da Silva Destinatário: Secretaria Municipal de Saúde Assunto: Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde. Colombo, 10 de fevereiro de 2020. VAGNER BRANDÃO Presidente"""
        dados = Lista().recuperar(conteudo)

        esperado = ['Nº 1 Ano 2020 Autor: Anderson Ferreira da Silva Destinatário: Secretaria Municipal de Saúde Assunto: Estudos para promover doações de bicicleta com tração compartilhada - motorizada e humana, para agentes comunitários de saúde.']

        self.assertEqual(esperado, dados)
