from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import ProjetoLei
from .serializers import ProjetoLeiSerializer


class ProjetoLeiViewSet(viewsets.ModelViewSet):
    queryset = ProjetoLei.objects.all().order_by('-projeto')
    serializer_class = ProjetoLeiSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60*23))
    def list(self, request):
        return super().list(request)

    @action(detail=False, methods=['GET'])
    def salvar(self, request):
        projeto = ProjetoLei()
        projeto.buscar_dados()
        return JsonResponse([], safe=False)

    @action(detail=False, methods=['GET'])
    def salvar_em_tramite(self, request):
        projeto = ProjetoLei()
        projeto.buscar_dados_em_tramite()
        return JsonResponse([], safe=False)

    @action(detail=False, methods=['GET'])
    def extrair_info(self, request):
        projeto = ProjetoLei()
        projeto.extrair_informacao()
        return JsonResponse([], safe=False)
