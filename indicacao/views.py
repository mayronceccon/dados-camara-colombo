import datetime
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Indicacao
from .serializers import IndicacaoSerializer
from .services1 import IndicacaoPautaServices


class IndicacaoViewSet(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all().order_by(
        '-pauta__data_sessao',
        '-numero'
    )
    serializer_class = IndicacaoSerializer
    http_method_names = ['get']

    # @method_decorator(cache_page(60*60*23))
    def retrieve(self, request, pk=None):
        """
        Retorna uma indicação específica
        """
        return super().retrieve(request, pk)

    # @method_decorator(cache_page(60*60*23))
    def list(self, request):
        """
        Retorna a lista de indicações
        """
        return super().list(request)

    @action(detail=False, methods=['GET'], name='Buscar Indicações')
    def buscar_indicacoes(self, request, *args, **kwargs):
        """
        Obtem as indicações das pautas da Câmara Municipal
        """
        services = IndicacaoPautaServices()
        services.buscar()
        return JsonResponse(
            datetime.datetime.now(),
            safe=False
        )
