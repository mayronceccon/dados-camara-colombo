from django.test import TestCase
from lib.util.json import is_json


class JsonTest(TestCase):
    def test_is_json(self):
        json = '{"nome": "Mayron"}'
        self.assertTrue(is_json(json))

    def test_is_not_json(self):
        json = 100
        self.assertFalse(is_json(json))
