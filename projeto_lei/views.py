from django.shortcuts import render
from django.http import JsonResponse
from .models import ProjetoLei


def salvar(request):
    ProjetoLei.buscar_dados()
    return JsonResponse([], safe=False)


def extrair_info(request):
    ProjetoLei.extrair_informacao()
    return JsonResponse([], safe=False)
