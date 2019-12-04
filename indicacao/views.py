import datetime
import json

from django.core import serializers
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.decorators import action
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

    @action(detail=False, methods=['GET'], name='Buscar Indicações')
    def buscar_indicacoes(self, request, *args, **kwargs):
        """Obter os PDF's do site da Câmara Municipal e salvar as indicações"""
        services = IndicacaoServices()
        services.buscar_indicacoes()
        return JsonResponse(
            datetime.datetime.now(),
            safe=False
        )

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
