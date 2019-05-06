from django.core.cache import cache
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets

from .models import Vereador
from .serializers import VereadorSerializer


class VereadorViewSet(viewsets.ModelViewSet):
    queryset = Vereador.objects.all().order_by('nome')
    serializer_class = VereadorSerializer
    http_method_names = ['get']
