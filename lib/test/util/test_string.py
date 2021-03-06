from django.test import TestCase
from lib.util.string import sanitize, normalize


class StringTest(TestCase):
    def test_sanitize(self):
        string = "Indicação número 2222 de João Pedro - 25/04/2011"
        esperado = "Indicacao numero 2222 de Joao Pedro 25 04 2011"
        self.assertEqual(esperado, sanitize(string))

    def test_normalize(self):
        string = """
           Indicação
           N°:222
           Autor:Renato Lunardon
           Destinatário: Secretaria de Urbanismo
           Assunto: Venho  solicitar  ao  setor  competente a
           viabilidade  de  construçãode  uma travessia
           elevada na  Rua Vereador  Angelim  Walesko  frente  ao  número  351,
           paralelas às  Ruas  Angelina Cavalli e Luiz Gasparin,
           no bairro Jardim Eucaliptos, neste município.

           Tribuna Livre: Darci Martins Braga. Assunto: COMESP –
           Consórcio Metropolitano de Saúde do Paraná.
        """
        conteudo_limpo = normalize(string)

        esperado = """Indicação N°:222 Autor:Renato Lunardon Destinatário: Secretaria de Urbanismo Assunto: Venho solicitar ao setor competente a viabilidade de construçãode uma travessia elevada na Rua Vereador Angelim Walesko frente ao número 351, paralelas às Ruas Angelina Cavalli e Luiz Gasparin, no bairro Jardim Eucaliptos, neste município. Tribuna Livre: Darci Martins Braga. Assunto: COMESP – Consórcio Metropolitano de Saúde do Paraná."""

        self.assertEqual(esperado, conteudo_limpo)
