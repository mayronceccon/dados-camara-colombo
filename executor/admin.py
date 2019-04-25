from django.contrib import admin
from .models import Executor


class ExecutorAdmin(admin.ModelAdmin):
    ordering = ('-nome',)
    fields = ('nome',)
    list_display = ['nome']

admin.site.register(Executor, ExecutorAdmin)
