from django.db import models
from pauta.models import Pauta
from executor.models import Executor
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
