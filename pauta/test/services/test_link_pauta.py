import os
from django.test import TestCase
from pauta.services.link_pauta import LinkPauta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LinkPautaTest(TestCase):
    def test_buscar_link(self):
        file = "%s/services/link_pauta.html" % (BASE_DIR)
        with open(file, 'r') as f:
            html = f.read()
        data = LinkPauta(html)

        expected = [
            {"title": "27/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=4"},
            {"title": "19/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=3"},
            {"title": "12/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=2"},
            {"title": "05/05/2020",
                "href": "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php?down=1"},
            {"title": "28/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_28_04_2020.pdf"},
            {"title": "22/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_22_04_2020.pdf"},
            {"title": "16/04/2020 - Extraordinária",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_16_04_2020.pdf"},
            {"title": "14/04/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_14_04_2020.pdf"},
            {"title": "17/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_17_03_2020.pdf"},
            {"title": "10/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_10_03_2020.pdf"},
            {"title": "03/03/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_03_03_2020.pdf"},
            {"title": "27/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_27_02_2020.pdf"},
            {"title": "18/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_18_02_2020.pdf"},
            {"title": "11/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_11_02_2020.pdf"},
            {"title": "04/02/2020",
                "href": "http://www.camaracolombo.pr.gov.br/pauta/2020/sessao_04_02_2020.pdf"},
        ]

        self.assertCountEqual(
            data.info(),
            expected
        )
