from django.contrib import admin
from .models import VereadorLink


class VereadorLinkAdmin(admin.ModelAdmin):
    fields = ('vereador', 'tipo', 'link', 'ano',)
    list_display = ['vereador', 'tipo', 'ano']

admin.site.register(VereadorLink, VereadorLinkAdmin)