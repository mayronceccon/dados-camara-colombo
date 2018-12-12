from django.contrib import admin
from .models import TipoSolicitacao


class TipoSolicitacaoAdmin(admin.ModelAdmin):
    ordering = ('-nome',)
    fields = ('nome',)
    list_display = ['nome']

admin.site.register(TipoSolicitacao, TipoSolicitacaoAdmin)