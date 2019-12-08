from django.test import TestCase
from ..models import Bairro


class BairroTest(TestCase):
    def setUp(self):
        Bairro.objects.create(
            id=1,
            nome='Canguiri',
            identificacao='canguiri'
        )

        Bairro.objects.create(
            id=2,
            nome='Colônia Farias',
            identificacao='colonia_faria'
        )

    def test_get_bairro(self):
        bairro = Bairro.objects.get(identificacao='canguiri')
        result = bairro.nome
        expected = 'Canguiri'
        self.assertEqual(expected, result)

        result = bairro.identificacao
        expected = 'canguiri'
        self.assertEqual(expected, result)

    def test_get_all_bairro(self):
        bairros = Bairro.objects.values_list('id', 'identificacao', 'nome')
        result = list(bairros[::1])
        expected = [
            (1, 'canguiri', 'Canguiri'),
            (2, 'colonia_faria', 'Colônia Farias')
        ]
        self.assertEqual(expected, result)
