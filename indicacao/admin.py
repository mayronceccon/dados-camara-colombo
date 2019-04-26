from django.contrib import admin
from .models import Indicacao


class IndicacaoAdmin(admin.ModelAdmin):
    ordering = ('-numero',)
    list_display = ['numero', 'pauta', 'vereador', 'destinatario']

admin.site.register(Indicacao, IndicacaoAdmin)
