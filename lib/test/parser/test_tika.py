import os
from django.test import TestCase
from unittest.mock import Mock, MagicMock
from tika import parser
from lib.parser.tika import Tika

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TikaTest(TestCase):
    def test_retorno_esperado(self):
        arquivo_texto_esperado = "%s/parser/texto_parser.txt" % (BASE_DIR)
        with open(arquivo_texto_esperado, 'r') as f:
            texto_esperado = f.read()

        link = "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_11_02_2020.pdf"

        parser_mock = Mock(spec=parser)
        parser_mock.from_file = Mock(return_value={'content': texto_esperado})

        parser_text = Tika(parser_mock)
        parser_text.set_link(link)
        texto = parser_text.get_text()

        parser_mock.from_file.assert_called_once_with(link)
        self.assertEqual(texto_esperado, texto)
