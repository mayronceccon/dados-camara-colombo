from django.db import models


class Pauta(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    link = models.URLField(unique=True, max_length=500)
    data_sessao = models.DateField()
    cadastro = models.DateField(auto_now=True)
