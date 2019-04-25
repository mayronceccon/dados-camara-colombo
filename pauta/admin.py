from django.contrib import admin
from .models import Pauta


class PautaAdmin(admin.ModelAdmin):
    ordering = ('-data_sessao',)
    fields = ('descricao', 'link', 'data_sessao', 'indicacao_exportada')
    list_display = ['descricao', 'data_sessao']
    date_hierarchy = 'data_sessao'

admin.site.register(Pauta, PautaAdmin)
