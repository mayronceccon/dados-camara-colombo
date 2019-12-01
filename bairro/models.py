from django.db import models


class Bairro(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    identificacao = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Identificação"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "bairro"
        verbose_name_plural = "bairros"
