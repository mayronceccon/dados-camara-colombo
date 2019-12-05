import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Pauta
from .serializers import PautaSerializer
from .services import PautaServices


class PautaViewSet(viewsets.ModelViewSet):
    queryset = Pauta.objects.all().order_by('-data_sessao')
    serializer_class = PautaSerializer
    http_method_names = ['get']

    @action(detail=False, methods=['GET'])
    def recuperar(self, request, *args, **kwargs):
        service = PautaServices()
        dados = service.busca_arquivos_sessao()
        return JsonResponse(dados, safe=False)

    @action(detail=False, methods=['GET'])
    def salvar(self, request, *args, **kwargs):
        service = PautaServices()
        service.salvar_busca()
        return JsonResponse([], safe=False)

    @method_decorator(cache_page(60*60*23))
    def list(self, request):
        return super().list(request)
