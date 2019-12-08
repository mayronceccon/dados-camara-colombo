from rest_framework import viewsets
from rest_framework import mixins
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Bairro
from .serializers import BairroSerializer


class BairroViewSet(viewsets.ModelViewSet):
    """Bairros do município de Colombo/PR"""
    queryset = Bairro.objects.all().order_by('nome')
    serializer_class = BairroSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(60*60*24*500))
    def list(self, request):
        return super().list(request)
