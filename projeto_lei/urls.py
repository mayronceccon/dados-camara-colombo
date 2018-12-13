from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salvar', views.salvar, name='salvar'),
    path('extrair_info', views.extrair_info, name='extrair_info'),
]
