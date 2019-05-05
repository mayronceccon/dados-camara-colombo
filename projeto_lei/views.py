from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets

from .models import ProjetoLei
from .serializers import ProjetoLeiSerializer


class ProjetoLeiViewSet(viewsets.ModelViewSet):
    queryset = ProjetoLei.objects.all().order_by('-projeto')
    serializer_class = ProjetoLeiSerializer
    http_method_names = ['get']


def index(request):
    cache_key = 'projetos_list'
    # 23 horas
    cache_time = (60 * 60 * 23)
    data = cache.get(cache_key)

    if not data:
        jsonresponse = []
        projetos = ProjetoLei.objects.all().order_by('-projeto')
        for projeto in projetos:
            jsonresponse.append({
                "projeto": projeto.projeto,
                "protocolo": projeto.protocolo,
                "assunto": projeto.assunto,
                "vereador": {
                    "nome": projeto.vereador.nome,
                    "apelino": projeto.vereador.apelido
                },
                "data_divulgacao": projeto.data_divulgacao,
                "data_aprovacao": projeto.data_aprovacao,
                "data_arquivamento": projeto.data_arquivamento
            })
        data = jsonresponse
        cache.set(cache_key, data, cache_time)

    return JsonResponse({"results": data})


def salvar(request):
    ProjetoLei.buscar_dados()
    return JsonResponse([], safe=False)


def salvar_em_tramite(request):
    ProjetoLei.buscar_dados_em_tramite()
    return JsonResponse([], safe=False)


def extrair_info(request):
    ProjetoLei.extrair_informacao()
    return JsonResponse([], safe=False)
