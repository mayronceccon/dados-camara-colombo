from django.contrib import admin
from .models import Indicacao


class IndicacaoAdmin(admin.ModelAdmin):
    ordering = ('-pauta', '-numero')
    list_display = ['numero', 'pauta', 'vereador', 'destinatario']
    list_filter = (
        'vereador',
        'pauta',
    )
    search_fields = ('numero', 'assunto', 'destinatario__nome')


admin.site.register(Indicacao, IndicacaoAdmin)
