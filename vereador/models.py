from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.core.cache import cache
from django.db.models import Q
import os
import uuid
import datetime
from multiselectfield import MultiSelectField
import unicodedata
import re
from lib.util.string import sanitize


class PatchedMultiSelectField(MultiSelectField):
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class VereadorManager(models.Manager):
    def buscar_nome(self, nome):
        vereadores = Vereador.objects.all()

        nome = sanitize(nome)
        for vereador in vereadores:
            nome_vereador = sanitize(vereador.nome)
            if (nome_vereador == nome):
                return vereador

            apelido_vereador = sanitize(vereador.apelido)
            if (apelido_vereador == nome):
                return vereador
        return None


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (uuid.uuid4(), slugify(instance.__str__()), ext)
    return os.path.join("vereador/", filename)


YEAR_CHOICES = []
for r in range(1995, (datetime.datetime.now().year+5)):
    YEAR_CHOICES.append((str(r), str(r)))


class Vereador(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    apelido = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone_gabinete = models.CharField(max_length=20, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    foto = models.ImageField(
        upload_to=content_file_name, null=True, blank=True)
    cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    legislaturas = PatchedMultiSelectField(
        choices=YEAR_CHOICES
    )
    objects = VereadorManager()

    def __str__(self):
        return "%s (%s)" % (self.nome, self.apelido)

    class Meta:
        verbose_name = "vereador"
        verbose_name_plural = "vereadores"

    def get_absolute_image_url(self):
        try:
            return "{0}{1}".format(Site.objects.get_current(), self.foto.url)
        except Exception:
            return None
