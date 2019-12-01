from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.cache import cache
from .models import Pauta
import json

from rest_framework import viewsets
from .serializers import PautaSerializer


class PautaViewSet(viewsets.ModelViewSet):
    queryset = Pauta.objects.all().order_by('-data_sessao')
    serializer_class = PautaSerializer
    http_method_names = ['get']


def index(request):
    cache_key = 'pauta_list'
    # 23 horas
    cache_time = (60 * 60 * 23)
    data = cache.get(cache_key)

    if not data:
        jsonresponse = []
        for pauta in Pauta.objects.all().order_by('-data_sessao'):
            jsonresponse.append({
                "id": pauta.id,
                "descricao": pauta.descricao,
                "link": pauta.link,
                "data_sessao": pauta.data_sessao
            })
        data = jsonresponse
        cache.set(cache_key, data, cache_time)

    return JsonResponse({"results": data})


def recuperar(request):
    pauta = Pauta()
    dados = pauta.busca_arquivos_sessao()
    return JsonResponse(dados, safe=False)


def salvar(request):
    pauta = Pauta()
    pauta.salvar_busca()
    return JsonResponse([], safe=False)
