from django.test import TestCase
from .models import Indicacao
from .models import Pauta
from .models import Vereador
from .services import IndicacaoServices


class IndicacaoTestCase(TestCase):
    def setUp(self):
        Pauta.objects.create(
            descricao="Sessão - 23/04/2019",
            link="http://www.camaracolombo.pr.gov.br/pauta/2019/sessao_23_04_2019.pdf",
            data_sessao="2019-04-23"
        )

        Pauta.objects.create(
            descricao="Sessão - 16/04/2019",
            link="http://www.camaracolombo.pr.gov.br/pauta/2019/sessao_16_04_2019.pdf",
            data_sessao="2019-04-16"
        )

        Vereador.objects.create(
            nome="Renato Lunardon",
            apelido="Renato Lunardon",
        )

        Vereador.objects.create(
            nome="Edson Luiz Bagio",
            apelido="Edson Baggio",
        )

        Vereador.objects.create(
            nome="Vagner Brandao",
            apelido="Vagner da Viação",
        )

        Vereador.objects.create(
            nome="Maurício Fortunato da Paixão",
            apelido="Issa",
        )

        Vereador.objects.create(
            nome="Sidinei Campos de Oliveira",
            apelido="Sidinei Campos",
        )

        Vereador.objects.create(
            nome="João Marcos Berlesi",
            apelido="Marquinho Berlesi",
        )

        Vereador.objects.create(
            nome="Anderson Ferreira da Silva",
            apelido="Anderson Prego",
        )

        Vereador.objects.create(
            nome="Eurico Braz de Bomfim",
            apelido="Eurico Dino",
        )

    def test_buscar_indicacoes_por_pauta(self):
        # service = IndicacaoServices()
        # indicacoes = service.buscar_indicacoes()
        self.assertTrue(True)

    def test_limpar_conteudo(self):
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

        service = IndicacaoServices()
        conteudo_limpo = service._limpar_conteudo(string)

        expected = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""

        self.assertEqual(expected.lstrip(), conteudo_limpo.lstrip())

    def test_recuperar_dados_lista(self):
        conteudo_limpo = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""

        service = IndicacaoServices()
        dados_lista = service._recuperar_dados_lista(conteudo_limpo.lstrip())

        expected = ['  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    ']

        self.assertEqual(expected, dados_lista)

    # def test_identificar_dados(self):
    #     dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

    #     service = IndicacaoServices()
    #     numero = service._indicacao_numero(dados)
    #     print(numero)

    #     self.assertEqual(222, numero)
