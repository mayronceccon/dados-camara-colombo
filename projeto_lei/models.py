from django.db import models
from vereador.models import Vereador


class ProjetoLei(models.Model):
    projeto = models.IntegerField()
    protocolo = models.IntegerField()
    assunto = models.TextField()
    observacao = models.TextField()
    vereador = models.ForeignKey(
        Vereador,
        on_delete=models.PROTECT
    )
    data_divulgacao = models.DateField(null=True, blank=True)
    data_aprovacao = models.DateField(null=True, blank=True)
    data_arquivamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.assunto
