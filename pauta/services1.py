from django.db import IntegrityError
from urllib.request import urlopen
from .models import Pauta
from .services.link_pauta import LinkPauta


class PautaServices:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def salvar_busca(self):
        dados = self.busca_arquivos_sessao()
        for dado in dados:
            try:
                pauta = Pauta(
                    descricao=dado['title'],
                    link=dado['href'],
                    data_sessao=dado['date']
                )
                pauta.save()
            except IntegrityError:
                error = "Registro ja existente - %s" % dado['title']
                print(error)

    def __urls(self):
        return "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php"

    def busca_arquivos_sessao(self):
        return self.__dados_html()

    def __dados_html(self):
        url_pauta = self.__urls()

        html = urlopen(url_pauta)
        data = LinkPauta(html.read())
        return data.info()
