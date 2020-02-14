from django.test import TestCase
from unittest.mock import Mock
from indicacao.models import Indicacao
from pauta.models import Pauta
from vereador.models import Vereador
from executor.models import Executor
from django.db.utils import IntegrityError


class IndicacaoModelsTest(TestCase):
    def setUp(self):
        self.__vereador = Vereador.objects.create(
            nome="Renato Lunardon",
            apelido="Renato Lunardon",
        )

        self.__pauta = Pauta.objects.create(
            descricao="Sessão - 23/04/2019",
            link="http://www.camaracolombo.pr.gov.br",
            data_sessao="2019-04-23"
        )

        self.__executor = Executor.objects.create(
            nome="NOME DO EXECUTOR"
        )

    def test_get_indicacao(self):
        indicacao = Indicacao(
            id=1,
            pauta=self.__pauta,
            vereador=self.__vereador,
            destinatario=self.__executor,
            numero=10,
            assunto="XPTO"
        )
        indicacao.save()

        indicacao = Indicacao.objects.get(pk=1)

        numero = indicacao.numero
        self.assertEquals(10, numero)

        assunto = indicacao.assunto
        self.assertEquals("XPTO", assunto)

        vereador = indicacao.vereador.nome
        self.assertEquals("Renato Lunardon", vereador)

        pauta = indicacao.pauta.descricao
        self.assertEquals("Sessão - 23/04/2019", pauta)

        executor = indicacao.destinatario.nome
        self.assertEquals("NOME DO EXECUTOR", executor)

    def test_get_all_indicacoes(self):
        indicacao = Indicacao(
            pauta=self.__pauta,
            vereador=self.__vereador,
            destinatario=self.__executor,
            numero=100,
            assunto="Assunto 100"
        )
        indicacao.save()

        indicacao = Indicacao(
            pauta=self.__pauta,
            vereador=self.__vereador,
            destinatario=self.__executor,
            numero=200,
            assunto="Assunto 200"
        )
        indicacao.save()

        indicacoes = Indicacao.objects.all()
        indicacoes_procura = [i.assunto for i in indicacoes]
        self.assertCountEqual(
            indicacoes_procura,
            ["Assunto 100", "Assunto 200"]
        )

        self.assertEqual(2, Indicacao.objects.count())

    def test_chaves_unicas(self):
        indicacao = Indicacao(
            pauta=self.__pauta,
            vereador=self.__vereador,
            destinatario=self.__executor,
            numero=100,
            assunto="Assunto 100"
        )
        indicacao.save()

        with self.assertRaises(IntegrityError):
            indicacao = Indicacao(
                pauta=self.__pauta,
                vereador=self.__vereador,
                destinatario=self.__executor,
                numero=100,
                assunto="Assunto 100"
            )
            indicacao.save()
