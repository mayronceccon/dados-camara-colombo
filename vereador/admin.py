from django.contrib import admin
from .models import Vereador


class VereadorAdmin(admin.ModelAdmin):
    ordering = ('-nome',)
    fields = ('nome', 'apelido', 'data_nascimento', 'email',
              'telefone_gabinete', 'observacao', 'foto', 'legislaturas',
              'ativo')
    list_display = ['nome', 'apelido']


admin.site.register(Vereador, VereadorAdmin)
