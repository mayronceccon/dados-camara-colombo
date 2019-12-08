from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from .models import Vereador
from .serializers import VereadorSerializer


class VereadorViewSet(viewsets.ModelViewSet):
    queryset = Vereador.objects.all().order_by('nome')
    serializer_class = VereadorSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60*24*30))
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @method_decorator(cache_page(60*60*23*30))
    def list(self, request):
        return super().list(request)
