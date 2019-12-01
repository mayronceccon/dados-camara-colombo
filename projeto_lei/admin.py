from django.contrib import admin
from .models import ProjetoLei


class ProjetoLeiAdmin(admin.ModelAdmin):
    ordering = ('-projeto',)
    fields = ('projeto', 'protocolo', 'assunto', 'observacao',
              'vereador', 'data_divulgacao', 'data_aprovacao',
              'data_arquivamento')
    list_display = ['projeto', 'assunto', 'data_divulgacao',
                    'data_aprovacao', 'data_arquivamento', 'vereador']


admin.site.register(ProjetoLei, ProjetoLeiAdmin)
