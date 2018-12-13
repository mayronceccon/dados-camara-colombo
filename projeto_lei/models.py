from django.db import models
from django.db import IntegrityError
from vereador.models import Vereador
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.db.models import Q
import re
from datetime import datetime


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
            situacao = str(tds[4])

            dados.append({
                'protocolo': protocolo,
                'projeto': projeto,
                'assunto': assunto,
                'situacao': situacao
            })
        return dados

    def remove_tupla(tuples):
        tuples = [t for t in tuples if t]
        return tuples

    def ajusta_data(data):
        if data is not None:
            data = str(data).replace('/', '-')
            data = datetime.strptime(data, '%d-%m-%Y')
            return data
        return None

    def extrair_informacao():
        projetos = ProjetoLei.objects.all().order_by('-projeto').exclude(
            Q(data_aprovacao__isnull=False) | Q(data_arquivamento__isnull=False)
        ).values()

        for projeto in projetos:
            observacao = projeto['observacao']
            aprovado = ProjetoLei.ajusta_data(ProjetoLei.indentifica_aprovacao(observacao))
            divulgado = ProjetoLei.ajusta_data(ProjetoLei.indentifica_divulgacao(observacao))
            arquivado = ProjetoLei.ajusta_data(ProjetoLei.indentifica_arquivamento(observacao))

            projeto_lei = ProjetoLei.objects.get(projeto=projeto['projeto'])
            projeto_lei.data_divulgacao = divulgado
            projeto_lei.data_aprovacao = aprovado
            projeto_lei.data_arquivamento = arquivado
            projeto_lei.save()

    def indentifica_aprovacao(observacao):
        regex1 = "(?:Aprovado<br\/>)([0-9]{2}\/[0-9]{2}\/[0-9]{4})"
        regex2 = "([0-9]{2}\/[0-9]{2}\/[0-9]{4}) - Aprovado<br\/>"
        regex3 = "Aprovado ([0-9]{2}\/[0-9]{2}\/[0-9]{4})"

        regex = r"%s|%s|%s" % (regex1, regex2, regex3)

        matches = re.findall(regex, observacao, re.IGNORECASE)
        for match in matches:
            return ProjetoLei.remove_tupla(match)[0]

    def indentifica_divulgacao(observacao):
        regex1 = "([0-9]{2}\/[0-9]{2}\/[0-9]{4}) - Divulgado"
        regex2 = "Divulgado - ([0-9]{2}\/[0-9]{2}\/[0-9]{4})"

        regex = r"%s|%s" % (regex1, regex2)

        matches = re.findall(regex, observacao, re.IGNORECASE)
        for match in matches:
            return ProjetoLei.remove_tupla(match)[0]

    def indentifica_arquivamento(observacao):
        regex1 = "(?:Arquivado<br\/>)([0-9]{2}\/[0-9]{2}\/[0-9]{4})"
        regex2 = "([0-9]{2}\/[0-9]{2}\/[0-9]{4})<br\/>Arquivado<br\/>"
        regex3 = "Arquivado - ([0-9]{2}\/[0-9]{2}\/[0-9]{4})"

        regex = r"%s|%s|%s" % (regex1, regex2, regex3)

        matches = re.findall(regex, observacao, re.IGNORECASE)
        for match in matches:
            return ProjetoLei.remove_tupla(match)[0]
