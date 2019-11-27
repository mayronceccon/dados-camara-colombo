from django.contrib import admin
from .models import Bairro


class BairroAdmin(admin.ModelAdmin):
    ordering = ('-nome',)
    fields = ('nome', 'identificacao',)
    list_display = ['nome', 'identificacao']


admin.site.register(Bairro, BairroAdmin)
