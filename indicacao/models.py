from django.db import models

from executor.models import Executor
from pauta.models import Pauta
from vereador.models import Vereador


class Indicacao(models.Model):
    pauta = models.ForeignKey(
        Pauta,
        on_delete=models.PROTECT,
        related_name='indicacoes'
    )

    vereador = models.ForeignKey(
        Vereador,
        on_delete=models.PROTECT,
        related_name='indicacoes',
        blank=True,
        null=True
    )

    destinatario = models.ForeignKey(
        Executor,
        on_delete=models.PROTECT,
        related_name='indicacoes'
    )

    numero = models.IntegerField()
    assunto = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.numero)

    class Meta:
        unique_together = ('numero', 'pauta')
