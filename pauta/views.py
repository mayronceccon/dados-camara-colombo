from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Pauta
import json
from django.core import serializers


def index(request):
    jsonresponse = []
    for pauta in Pauta.objects.all().order_by('-data_sessao'):
        jsonresponse.append({
            "id": pauta.id,
            "descricao": pauta.descricao,
            "link": pauta.link,
            "data_sessao": pauta.data_sessao
        })

    return JsonResponse({"results": jsonresponse})


def recuperar(request):
    dados = Pauta.busca_arquivos_sessao()
    return JsonResponse(dados, safe=False)


def salvar(request):
    Pauta.salvar_busca()
    return JsonResponse([], safe=False)
