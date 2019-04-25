from django.db import models
from django.db import IntegrityError
from pauta.models import Pauta
from executor.models import Executor
from vereador.models import Vereador
from tika import parser
import re


class Indicacao(models.Model):
    pauta = models.ForeignKey(
        Pauta,
        on_delete=models.PROTECT,
        related_name='indicacoes'
    )

    vereador = models.ForeignKey(
        Vereador,
        on_delete=models.PROTECT,
        related_name='indicacoes'
    )

    destinatario = models.ForeignKey(
        Executor,
        on_delete=models.PROTECT,
        related_name='indicacoes'
    )

    numero = models.IntegerField(unique=True)
    assunto = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.numero

    def buscar_indicacoes():
        pautas = Pauta.objects.all().filter(indicacao_exportada=False)
        for pauta in pautas:
            try:
                Indicacao.buscar_dados(pauta)
                pauta.indicacao_exportada = True
                pauta.save()
            except IntegrityError:
                pass

        return True

    def buscar_dados(pauta):
        url = pauta.link
        raw = parser.from_file(url)

        content = raw['content']
        content = content.strip().rstrip('\r\n').replace("\n", "").replace("\r", "").replace("  ", " ")
        content = content.strip().rstrip('\r\n').replace("\n", "").replace("\r", "").replace("  ", " ")

        regex = r"(?:cação\s)(.*?)(?:\sIndi|\sColombo, [0-9]{1,2} de)"
        matches = re.findall(regex, content)
        if matches is not None:
            for match in matches:
                numero = Indicacao.indicacao_numero(match)
                autor = Indicacao.indicacao_autor(match)
                destinatario = Indicacao.indicacao_destinatario(match)
                assunto = Indicacao.indicacao_assunto(match)

                autor = autor.split("(")
                autor = autor[0].strip()

                vereador = Vereador.buscar_nome(autor)
                obj, created = Executor.objects.get_or_create(
                    nome=destinatario
                )

                indicacao = Indicacao(
                    pauta=pauta,
                    vereador=vereador,
                    destinatario=obj,
                    numero=numero,
                    assunto=assunto
                )
                indicacao.save()

    def indicacao_numero(indicacao):
        regex = r"((?:N°[:]?\s)([0-9]{1,})(?:\sAutor))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            return matches.group(2)

    def indicacao_autor(indicacao):
        regex = r"((?:Autor[:]?\s|Autora[:]?\s)(.*)(?:\sDestinatário))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            return matches.group(2)

    def indicacao_destinatario(indicacao):
        regex = r"((?:Destinatário[:]?\s)(.*)(?:\sAssunto:))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            return matches.group(2)

    def indicacao_assunto(indicacao):
        regex = r"((?:Assunto[:]?\s)(.*))"
        matches = re.search(regex, indicacao)
        if matches is not None:
            return matches.group(2)
