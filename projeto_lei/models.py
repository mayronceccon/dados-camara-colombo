from django.db import models
from django.db import IntegrityError
from vereador.models import Vereador
from bs4 import BeautifulSoup
from urllib.request import urlopen


class ProjetoLei(models.Model):
    projeto = models.IntegerField(unique=True)
    protocolo = models.IntegerField(unique=True)
    assunto = models.TextField()
    observacao = models.TextField()
    vereador = models.ForeignKey(
        Vereador,
        on_delete=models.PROTECT,
        related_name='projetos'
    )
    data_divulgacao = models.DateField(null=True, blank=True)
    data_aprovacao = models.DateField(null=True, blank=True)
    data_arquivamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.assunto

    def buscar_dados():
        vereadores = Vereador.objects.all()
        for vereador in vereadores:
            link_projeto = vereador.links.all().filter(tipo=1).values()
            if link_projeto:
                link = link_projeto[0]['link']
                dados = ProjetoLei.buscar_html(link)
                for dado in dados:
                    try:
                        projeto_lei = ProjetoLei(
                            projeto=dado['projeto'],
                            protocolo=dado['protocolo'],
                            assunto=dado['assunto'],
                            observacao=dado['situacao'],
                            vereador=vereador
                        )
                        projeto_lei.save()
                    except IntegrityError:
                        projeto_lei = ProjetoLei.objects.get(projeto=dado['projeto'])
                        projeto_lei.observacao = dado['situacao']
                        projeto_lei.save()
                        error = "Projeto ja existente - %s" % dado['projeto']
                        print(error)

    def buscar_html(link):
        html = urlopen(link)
        res = BeautifulSoup(html.read(), "html5lib")

        tables = res.find_all(
            "table",
            {
                "id": "table48"
            }
        )

        dados = []
        for table in tables:
            tds = table.find_all(
                "td"
            )
            protocolo = tds[0].get_text().strip()

            projeto = tds[1].get_text().strip()
            projeto = projeto.split('/')
            projeto = projeto[0]

            assunto = tds[3].get_text().strip()
            situacao = tds[4].get_text().strip()

            dados.append({
                'protocolo': protocolo,
                'projeto': projeto,
                'assunto': assunto,
                'situacao': situacao
            })
        return dados
