from django.test import TestCase, Client
from rest_framework import status
from ..models import Bairro
from ..serializers import BairroSerializer

client = Client()


class BairroTest(TestCase):
    def setUp(self):
        Bairro.objects.create(
            id=1,
            nome='Canguiri',
            identificacao='canguiri'
        )

    def test_get_all_bairros(self):
        response = client.get('/api/v1/bairros/')
        bairro = Bairro.objects.all()
        serializer = BairroSerializer(bairro, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_bairro(self):
        pk = 1
        response = client.get(f'/api/v1/bairros/{pk}/')
        bairro = Bairro.objects.get(pk=pk)
        serializer = BairroSerializer(bairro)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_404_specific_bairro(self):
        pk = 404
        response = client.get(f'/api/v1/bairros/{pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
