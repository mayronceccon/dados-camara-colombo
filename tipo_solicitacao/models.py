from django.db import models


class TipoSolicitacao(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "tipo de solicitação"
        verbose_name_plural = "tipos de solicitação"
