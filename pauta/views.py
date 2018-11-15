from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Pauta
import json
from django.core import serializers


def index(request):
    dados = (
        Pauta.objects
        .order_by('-data_sessao')
        .filter()
        .values('id', 'descricao', 'link', 'data_sessao')
    )
    pautas_list = list(dados)
    return JsonResponse(pautas_list, safe=False)


def recuperar(request):
    dados = Pauta.busca_arquivos_sessao()
    return JsonResponse(dados, safe=False)


def salvar(request):
    Pauta.salvar_busca()
    return JsonResponse([], safe=False)
