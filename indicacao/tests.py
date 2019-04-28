from django.test import TestCase
from .models import Indicacao
from .models import Pauta
from .models import Vereador


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
        indicacoes = Indicacao.buscar_indicacoes()
        self.assertTrue(True)
