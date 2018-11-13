from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from django.db import IntegrityError
from datetime import datetime
from .models import Pauta


def urls():
    url_camara = 'http://www.camaracolombo.pr.gov.br'
    url_pauta = "%s/pauta.html" % (url_camara)
    return {
        'camara': url_camara,
        'pauta': url_pauta
    }


def index(request):
    url_camara = urls()['camara']
    sessoes = dadosHtml()
    dados = []
    for sessao in sessoes:
        href = sessao['href']
        arquivo_sessao = arquivoSessao(sessao)

        # busca nomes arquivos
        regex = r"(/sessao_)(.*)(.pdf)"
        matches = re.search(regex, href)
        nome_arquivo = matches.group(2).replace('_', '-')

        # titulo = nome_arquivo
        
        # busca datas
        data = nome_arquivo
        regex2 = r"(\d{2}-\d{2}-\d{4})-(\d{0,})"
        matches = re.search(regex2, data)
        if matches is not None:
            data = matches.group(1)
            # compl = 'Extraordinária'
            # titulo = "%s - %s" % (data, compl)

        data2 = datetime.strptime(data, '%d-%m-%Y')
        titulo = data2.strftime("%d/%m/%Y")

        dados.append({
            'titulo': titulo,
            'data': data2,
            'arquivo': arquivo_sessao
        })

        # try:
        #     pauta = Pauta(descricao=data_sessao, link=arquivo_sessao)
        #     pauta.save()
        # except IntegrityError:
        #     print('aaa')
    return JsonResponse(dados, safe=False)


def dadosHtml():
    url_camara = urls()['camara']
    url_pauta = urls()['pauta']

    html = urlopen(url_pauta)
    res = BeautifulSoup(html.read(), "html5lib")

    sessoes = res.find_all("a", {"href": re.compile(r'(^pauta)(.*)(.pdf$)')})
    return sessoes


def buscaData():
    pass


def arquivoSessao(sessao):
    url_camara = urls()['camara']
    href = sessao['href']
    arquivo_sessao = "%s/%s" % (url_camara, href)
    return arquivo_sessao


def dadosSessao():
    pass
