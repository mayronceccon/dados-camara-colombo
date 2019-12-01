from django.db import models
from django.db import IntegrityError
from django.core.cache import cache
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import re
from lib.notificacao import send


class Pauta(models.Model):
    descricao = models.CharField(max_length=100)
    link = models.URLField(max_length=255, unique=True)
    data_sessao = models.DateField()
    cadastro = models.DateTimeField(auto_now_add=True)
    indicacao_exportada = models.BooleanField(
        default=False,
        verbose_name=u'Indicacoes Exportadas'
    )

    def __str__(self):
        return self.descricao

    def save(self, *args, **kwargs):
        cache_key = 'pauta_list'
        cache.delete(cache_key)
        super(Pauta, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "pauta"
        verbose_name_plural = "pautas"

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
        url_camara = 'http://www.camaracolombo.pr.gov.br'
        url_pauta = "%s/pauta.html" % (url_camara)
        return {
            'camara': url_camara,
            'pauta': url_pauta
        }

    def busca_arquivos_sessao(self):
        url_camara = self.__urls()['camara']
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
        url_camara = self.__urls()['camara']
        url_pauta = self.__urls()['pauta']

        html = urlopen(url_pauta)
        res = BeautifulSoup(html.read(), "html5lib")

        sessoes = res.find_all(
            "a",
            {
                "href": re.compile(r'(^pauta)(.*)(.pdf$)')
            }
        )
        return sessoes

    def __arquivo_sessao(self, sessao):
        url_camara = self.__urls()['camara']
        href = sessao['href']
        arquivo_sessao = "%s/%s" % (url_camara, href)
        return arquivo_sessao
