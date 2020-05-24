import re
from bs4 import BeautifulSoup


class LinkPauta:
    def __init__(self, html):
        self.__html = html

    def info(self):
        res = BeautifulSoup(self.__html, "html5lib")

        titles = res.find_all(
            "font",
            string=re.compile(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}')
        )
        sessoes = []
        for title in titles:
            t = title.text.strip()
            href = title.find_parent("a")["href"]

            regex = r"\?down=[0-9]{1,}"
            matches = re.search(regex, href)
            if matches is not None:
                href = f"http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php{href}"

            sessoes.append({
                "title": t,
                "href": href
            })
        return sessoes
