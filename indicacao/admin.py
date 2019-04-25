from django.contrib import admin
from .models import Indicacao


class IndicacaoAdmin(admin.ModelAdmin):
    ordering = ('-numero',)

admin.site.register(Indicacao, IndicacaoAdmin)
