from django.db import models
import unicodedata
import re


def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', ' ', palavraSemAcento)


class Executor(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        nome = self.nome.upper()
        nome = removerAcentosECaracteresEspeciais(nome)
        self.nome = nome
        super(Executor, self).save(*args, **kwargs)
