import datetime
import json

from django.core import serializers
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import viewsets

from .models import Indicacao
from .serializers import IndicacaoSerializer
from .services import IndicacaoServices


class IndicacaoViewSet(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all().order_by(
        '-pauta__data_sessao',
        '-numero'
    )
    serializer_class = IndicacaoSerializer
    http_method_names = ['get']

    def get_queryset(self):
        vereador = self.request.query_params.get('vereador', None)
        if vereador is not None:
            find = (
                Q(vereador__nome__icontains=vereador) | 
                Q(vereador__apelido__icontains=vereador)
            )
            if vereador.isnumeric():
                find = Q(vereador=vereador)
            self.queryset = self.queryset.filter(find)

        pauta = self.request.query_params.get('pauta', None)
        if pauta is not None:
            find = Q(pauta__descricao__icontains=pauta)
            if pauta.isnumeric():
                find = Q(pauta=pauta)
            self.queryset = self.queryset.filter(find)

        destinatario = self.request.query_params.get('destinatario', None)
        if destinatario is not None:
            find = Q(destinatario__nome__icontains=destinatario)
            if destinatario.isnumeric():
                find = Q(destinatario=destinatario)
            self.queryset = self.queryset.filter(find)

        assunto = self.request.query_params.get('assunto', None)
        if assunto is not None:
            find = Q(assunto__icontains=assunto)
            self.queryset = self.queryset.filter(find)
        return self.queryset


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
