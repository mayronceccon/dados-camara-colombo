from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recuperar', views.recuperar, name='recuperar'),
    path('salvar', views.salvar, name='salvar'),
]
