from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salvar', views.salvar, name='salvar'),
    path('salvar_em_tramite', views.salvar_em_tramite, name='salvar_em_tramite'),
    path('extrair_info', views.extrair_info, name='extrair_info'),
]
