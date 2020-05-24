import re
from bs4 import BeautifulSoup
from datetime import datetime


class LinkPauta:
    def __init__(self, html):
        self.__html = html

    def info(self):
        res = BeautifulSoup(self.__html, "html5lib")

        list_pautas = res.find_all(
            "font",
            string=re.compile(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}')
        )
        sessoes = []
        for pauta in list_pautas:
            title = pauta.text.strip()
            date = self.__get_date(title)
            href = pauta.find_parent("a")["href"]
            href = self.__href_process(href)

            sessoes.append({
                "title": title,
                "href": href,
                "date": date
            })
        return sessoes

    def __href_process(self, href):
        regex = r"\?down=[0-9]{1,}"
        matches = re.search(regex, href)
        if matches is not None:
            href = f"http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php{href}"
        return href

    def __get_date(self, title):
        d = title.split("-")[0].strip()
        return datetime.strptime(d, '%d/%m/%Y')
