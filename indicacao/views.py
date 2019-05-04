import json
import datetime

from django.core import serializers
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Indicacao
from .serializers import IndicacaoSerializer
from .services import IndicacaoServices


class IndicacaoViewSet(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all().order_by('-numero')
    serializer_class = IndicacaoSerializer
    http_method_names = ['get']


def index(request):
    cache_key = 'indicacao_list'
    # 23 horas
    cache_time = (60 * 60 * 23)
    data = cache.get(cache_key)

    if not data:
        jsonresponse = []
        for indicacao in Indicacao.objects.all().order_by('-numero'):
            vereador = None
            if indicacao.vereador:
                vereador = {
                    "id": indicacao.vereador.id,
                    "nome": indicacao.vereador.nome,
                    "apelido": indicacao.vereador.apelido
                }

            jsonresponse.append({
                "id": indicacao.id,
                "numero": indicacao.numero,
                "assunto": indicacao.assunto,
                "pauta": {
                    "id": indicacao.pauta.id,
                    "data": indicacao.pauta.data_sessao,
                    "descricao": indicacao.pauta.descricao
                },
                "destinatario": {
                    "id": indicacao.destinatario.id,
                    "descricao": indicacao.destinatario.nome
                },
                "vereador": vereador
            })
        data = jsonresponse
        cache.set(cache_key, data, cache_time)

    return JsonResponse({"results": data})


def buscar_indicacoes(request):
    services = IndicacaoServices()
    services.buscar_indicacoes()
    return JsonResponse(
        datetime.datetime.now(),
        safe=False
    )
