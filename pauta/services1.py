from django.db import IntegrityError
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
from lib.notificacao import send
import re

from .models import Pauta
from .services.link_pauta import LinkPauta


class PautaServices:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def salvar_busca(self):
        dados = self.busca_arquivos_sessao()
        notificar = False
        for dado in dados:
            try:
                descricao = dado['titulo']
                pauta = Pauta(
                    descricao=descricao,
                    link=dado['arquivo'],
                    data_sessao=dado['data']
                )
                pauta.save()
                notificar = True
            except IntegrityError:
                error = "Registro ja existente - %s" % dado['titulo']
                print(error)

        if notificar:
            send.enviar(
                "Nova Pauta disponível - %s" % (descricao),
                'https://camaracolombo.com.br/pautas'
            )

    def __urls(self):
        url_pauta = "http://www.midias.camaracolombo.pr.gov.br/edital_sessoes.php"
        return {
            'pauta': url_pauta
        }

    def busca_arquivos_sessao(self):
        sessoes = self.__dados_html()
        dados = []
        for sessao in sessoes:
            compl = None
            titulo = None
            href = sessao['href']
            arquivo_sessao = self.__arquivo_sessao(sessao)

            # busca nomes arquivos
            regex = r"(/sessao_)(.*)(.pdf)"
            matches = re.search(regex, href)
            data = matches.group(2).replace('_', '-')

            # busca datas
            regex2 = r"(\d{2}-\d{2}-\d{4})-(\d{0,})"
            matches = re.search(regex2, data)
            if matches is not None:
                data = matches.group(1)
                compl = 'Extraordinária'

            # titulo
            data = datetime.strptime(data, '%d-%m-%Y')
            titulo = data.strftime("%d/%m/%Y")
            if compl is not None:
                titulo = "%s - %s" % (titulo, compl)

            titulo = "Sessão - %s" % titulo

            dados.append({
                'titulo': titulo,
                'data': data,
                'arquivo': arquivo_sessao
            })
        return dados

    def __dados_html(self):
        url_pauta = self.__urls()['pauta']

        html = urlopen(url_pauta)
        data = LinkPauta(html.read())
        return data.info()

    def __arquivo_sessao(self, sessao):
        return sessao['href']
