from django.db import models
from lib.util.string import sanitize
import unicodedata
import re


class Executor(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        nome = self.nome.upper()
        nome = sanitize(nome)
        self.nome = nome
        super(Executor, self).save(*args, **kwargs)
