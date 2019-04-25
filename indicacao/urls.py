from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar_indicacoes', views.buscar_indicacoes, name='buscar_indicacoes'),
]
