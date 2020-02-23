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
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


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

    @action(detail=False, methods=['GET'], name='Indicações por Bairros')
    def bairros(self, request, *args, **kwargs):
        """
        Total de indicações por bairro
        """
        rows = []
        with connection.cursor() as cursor:
            sql = """
                select
                b.nome as bairro,
                count(*) as indicacoes
                from bairro_bairro as b
                inner join indicacao_indicacao as i on i.assunto like CONCAT('%', b.nome, '%')
                group by b.nome
                order by indicacoes desc
            """
            cursor.execute(sql)
            rows = dictfetchall(cursor)

        return JsonResponse(
            rows,
            safe=False
        )

    @action(detail=False, methods=['GET'], name='Indicações dos Vereadores por Bairro')
    def vereadores_bairros(self, request, *args, **kwargs):
        """
        Total de indicações dos vereadores por bairros
        """
        rows = []
        with connection.cursor() as cursor:
            sql = """
                select
                b.nome as bairro,
                CONCAT(v.nome, ' (', v.apelido, ')') as vereador,
                count(*) as indicacoes
                from bairro_bairro as b
                inner join indicacao_indicacao as i on i.assunto like CONCAT('%', b.nome, '%')
                inner join vereador_vereador as v on v.id = i.vereador_id
                group by b.nome, i.vereador_id
                order by indicacoes desc
            """
            cursor.execute(sql)
            rows = dictfetchall(cursor)

        return JsonResponse(
            rows,
            safe=False
        )
