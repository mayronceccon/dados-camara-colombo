from django.test import TestCase
from .models import Indicacao
from .models import Pauta
from .models import Vereador
from .services import IndicacaoServices


class IndicacaoTestCase(TestCase):
    # def setUp(self):
    #     Pauta.objects.create(
    #         descricao="Sessão - 23/04/2019",
    #         link="http://www.camaracolombo.pr.gov.br/pauta/2019/sessao_23_04_2019.pdf",
    #         data_sessao="2019-04-23"
    #     )

    #     Pauta.objects.create(
    #         descricao="Sessão - 16/04/2019",
    #         link="http://www.camaracolombo.pr.gov.br/pauta/2019/sessao_16_04_2019.pdf",
    #         data_sessao="2019-04-16"
    #     )

    #     Vereador.objects.create(
    #         nome="Renato Lunardon",
    #         apelido="Renato Lunardon",
    #     )

    #     Vereador.objects.create(
    #         nome="Edson Luiz Bagio",
    #         apelido="Edson Baggio",
    #     )

    #     Vereador.objects.create(
    #         nome="Vagner Brandao",
    #         apelido="Vagner da Viação",
    #     )

    #     Vereador.objects.create(
    #         nome="Maurício Fortunato da Paixão",
    #         apelido="Issa",
    #     )

    #     Vereador.objects.create(
    #         nome="Sidinei Campos de Oliveira",
    #         apelido="Sidinei Campos",
    #     )

    #     Vereador.objects.create(
    #         nome="João Marcos Berlesi",
    #         apelido="Marquinho Berlesi",
    #     )

    #     Vereador.objects.create(
    #         nome="Anderson Ferreira da Silva",
    #         apelido="Anderson Prego",
    #     )

    #     Vereador.objects.create(
    #         nome="Eurico Braz de Bomfim",
    #         apelido="Eurico Dino",
    #     )

    def test_recuperar_conteudo(self):
        arquivo = './indicacao/sessao_23_04_2019.pdf'

        service = IndicacaoServices()
        conteudo = service._recuperar_conteudo(arquivo)

        lista = service._recuperar_dados_lista(conteudo)

        # INDICACAO 1
        item = lista[0]

        numero = service._indicacao_numero(item)
        self.assertEqual(223, numero)

        autor = service._indicacao_autor(item)
        self.assertEqual('Renato Lunardon', autor)

        destinatario = service._indicacao_destinatario(item)
        self.assertEqual('SECRETARIA DE GOVERNO', destinatario)

        assunto_esperado = 'Venho solicitar a esta secretaria para que viabilize junto a Copel para a troca de alguns postes de luz da rede elétrica, bem como a substituição das luminárias existentes por novas com lâmpadas de LED de 200 watts, na Rua Presidente Faria, desde o início da Estrada da Ribeira até a Rodovia Régis Bittencourt, bairro Colônia Faria, neste município.'
        assunto = service._indicacao_assunto(item)
        self.assertEqual(assunto_esperado, assunto)

        # INDICACAO 2
        item = lista[10]

        numero = service._indicacao_numero(item)
        self.assertEqual(233, numero)

        autor = service._indicacao_autor(item)
        self.assertEqual('Vagner Brandão', autor)

        destinatario = service._indicacao_destinatario(item)
        self.assertEqual('SECRETARIA DE PLANEJAMENTO', destinatario)

        assunto_esperado = 'Pavimentação asfáltica da Rua da Arara, no bairro Arruda, em Colombo/PR.'
        assunto = service._indicacao_assunto(item)
        self.assertEqual(assunto_esperado, assunto)

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

        experado = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""

        self.assertEqual(experado.lstrip(), conteudo_limpo.lstrip())

    def test_recuperar_dados_lista(self):
        conteudo_limpo = """Indicação   N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.     Tribuna Livre: Darci Martins Braga. Assunto: COMESP –   Consórcio Metropolitano de Saúde do Paraná."""

        service = IndicacaoServices()
        dados_lista = service._recuperar_dados_lista(conteudo_limpo.lstrip())

        experado = ['  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    ']

        self.assertEqual(experado, dados_lista)

    def test_identificar_dados(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

        service = IndicacaoServices()
        numero = service._indicacao_numero(dados)

        experado = 222

        self.assertEqual(experado, numero)

    def test_identificar_autor(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

        service = IndicacaoServices()
        autor = service._indicacao_autor(dados)

        experado = 'Renato Lunardon'

        self.assertEqual(experado, autor)

    def test_identificar_destinatario(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

        service = IndicacaoServices()
        destinatario = service._indicacao_destinatario(dados)

        experado = 'SECRETARIA DE URBANISMO'

        self.assertEqual(experado, destinatario)

    def test_identificar_assunto(self):
        dados = '  N°:222   Autor:Renato Lunardon   Destinatário: Secretaria de Urbanismo   Assunto: Venho solicitar ao setor competente a   viabilidade de construçãode uma travessia   elevada na Rua Vereador Angelim Walesko frente ao número 351,   paralelas às Ruas Angelina Cavalli e Luiz Gasparin,   no bairro Jardim Eucaliptos, neste município.    '

        service = IndicacaoServices()
        assunto = service._indicacao_assunto(dados)

        experado = 'Venho solicitar ao setor competente a viabilidade de construçãode uma travessia elevada na Rua Vereador Angelim Walesko frente ao número 351, paralelas às Ruas Angelina Cavalli e Luiz Gasparin, no bairro Jardim Eucaliptos, neste município.'

        self.assertEqual(experado, assunto)
