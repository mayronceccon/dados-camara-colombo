import datetime
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework import viewsets
from .models import Indicacao
from .serializers import IndicacaoSerializer
from .services1 import IndicacaoPautaServices


class IndicacaoViewSet(viewsets.ModelViewSet):
    serializer_class = IndicacaoSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Indicacao.objects.all().order_by(
            '-pauta__data_sessao',
            '-numero'
        )
        assunto = self.request.query_params.get('assunto', None)
        if assunto is not None:
            queryset = queryset.filter(
                assunto__icontains=assunto
            )

        destinatario = self.request.query_params.get('destinatario', None)
        if destinatario is not None:
            queryset = queryset.filter(
                destinatario__nome__icontains=destinatario
            )

        vereador = self.request.query_params.get('vereador', None)
        if vereador is not None:
            if vereador.isnumeric():
                queryset = queryset.filter(
                    vereador__id=vereador
                )
            else:
                queryset = queryset.filter(
                    Q(vereador__nome__icontains=vereador) |
                    Q(vereador__apelido__icontains=vereador)
                )

        return queryset

    @method_decorator(cache_page(60*60*23))
    def retrieve(self, request, pk=None):
        """
        Retorna uma indicação específica
        """
        return super().retrieve(request, pk)

    @method_decorator(cache_page(60*60*23))
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
