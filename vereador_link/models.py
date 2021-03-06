from django.db import models
import datetime
from vereador.models import Vereador
from tipo_solicitacao.models import TipoSolicitacao

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


def current_year():
    return datetime.date.today().year


class VereadorLink(models.Model):
    vereador = models.ForeignKey(
        Vereador,
        on_delete=models.PROTECT,
        related_name='links'
    )
    tipo = models.ForeignKey(
        TipoSolicitacao,
        on_delete=models.PROTECT
    )
    link = models.URLField(max_length=500)
    ano = models.IntegerField(
        choices=YEAR_CHOICES,
        default=current_year,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.link
    
    class Meta:
        verbose_name = "link de vereador"
        verbose_name_plural = "links de vereadores"
