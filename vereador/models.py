from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
import os
import uuid


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (uuid.uuid4(), slugify(instance.__str__()), ext)
    return os.path.join("vereador/", filename)


class Vereador(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    apelido = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone_gabinete = models.CharField(max_length=20, null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_absolute_image_url(self):
        return "{0}{1}".format(Site.objects.get_current(), self.foto.url)
