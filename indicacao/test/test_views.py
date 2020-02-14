from django.test import TestCase, Client
from rest_framework import status
from lib.util.json import is_json
from indicacao.models import Indicacao
from indicacao.serializers import IndicacaoSerializer
from pauta.models import Pauta
from vereador.models import Vereador
from executor.models import Executor

client = Client()


class IndicacaoViewsTest(TestCase):
    def setUp(self):
        vereador = Vereador.objects.create(
            nome="Renato Lunardon",
            apelido="Renato Lunardon",
        )

        pauta = Pauta.objects.create(
            descricao="Sessão - 23/04/2019",
            link="http://www.camaracolombo.pr.gov.br",
            data_sessao="2019-04-23"
        )

        executor = Executor.objects.create(
            nome="NOME DO EXECUTOR"
        )

        indicacao = Indicacao(
            id=1,
            pauta=pauta,
            vereador=vereador,
            destinatario=executor,
            numero=100,
            assunto="Assunto 100"
        )
        indicacao.save()

        indicacao = Indicacao(
            id=2,
            pauta=pauta,
            vereador=vereador,
            destinatario=executor,
            numero=200,
            assunto="Assunto 200"
        )
        indicacao.save()

    def test_get_all_indicacoes(self):
        response = client.get('/api/v1/indicacoes/')

        indicacoes = Indicacao.objects.all()
        serializer = IndicacaoSerializer(indicacoes, many=True)

        self.assertCountEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_json(response.content))

    def test_get_indicacao(self):
        pk = 1
        response = client.get(f'/api/v1/indicacoes/{pk}/')
        indicacao = Indicacao.objects.get(pk=1)

        self.assertEqual(1, response.data['id'])
        self.assertEqual(100, response.data['numero'])
        self.assertEqual("Assunto 100", response.data['assunto'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_json(response.content))

    def test_get_indicacao_404(self):
        pk = 404
        response = client.get(f'/api/v1/indicacoes/{pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_busca_indicacoes(self):
        response = client.get('/api/v1/indicacoes/buscar_indicacoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_json(response.content))
