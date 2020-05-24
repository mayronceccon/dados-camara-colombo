import os
from django.test import TestCase
from pauta.services.link_pauta import LinkPauta
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LinkPautaTest(TestCase):
    def test_buscar_link(self):
        file = "%s/services/link_pauta.html" % (BASE_DIR)
        with open(file, 'r') as f:
            html = f.read()
        data = LinkPauta(html)

        expected = [
            {
                "title": "27/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=4",
                "date": datetime.datetime(2020, 5, 27, 0, 0)
            },
            {
                "title": "19/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=3",
                "date": datetime.datetime(2020, 5, 19, 0, 0)
            },
            {
                "title": "12/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=2",
                "date": datetime.datetime(2020, 5, 12, 0, 0)
            },
            {
                "title": "05/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=1",
                "date": datetime.datetime(2020, 5, 5, 0, 0)
            },
            {
                "title": "28/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_28_04_2020.pdf",
                "date": datetime.datetime(2020, 4, 28, 0, 0)
            },
            {
                "title": "22/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_22_04_2020.pdf",
                "date": datetime.datetime(2020, 4, 22, 0, 0)
            },
            {
                "title": "16/04/2020 - Extraordinária",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_16_04_2020.pdf",
                "date": datetime.datetime(2020, 4, 16, 0, 0)
            },
            {
                "title": "14/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_14_04_2020.pdf",
                "date": datetime.datetime(2020, 4, 14, 0, 0)
            },
            {
                "title": "17/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_17_03_2020.pdf",
                "date": datetime.datetime(2020, 3, 17, 0, 0)
            },
            {
                "title": "10/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_10_03_2020.pdf",
                "date": datetime.datetime(2020, 3, 10, 0, 0)
            },
            {
                "title": "03/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_03_03_2020.pdf",
                "date": datetime.datetime(2020, 3, 3, 0, 0)
            },
            {
                "title": "27/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_27_02_2020.pdf",
                "date": datetime.datetime(2020, 2, 27, 0, 0)
            },
            {
                "title": "18/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_18_02_2020.pdf",
                "date": datetime.datetime(2020, 2, 18, 0, 0)
            },
            {
                "title": "11/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_11_02_2020.pdf",
                "date": datetime.datetime(2020, 2, 11, 0, 0)
            },
            {
                "title": "04/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_04_02_2020.pdf",
                "date": datetime.datetime(2020, 2, 4, 0, 0)
            },
        ]

        self.assertCountEqual(
            data.info(),
            expected
        )
