from rest_framework import viewsets
from rest_framework import mixins

from .models import Bairro
from .serializers import BairroSerializer


class BairroViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """Bairros do município de Colombo/PR"""
    queryset = Bairro.objects.all().order_by('nome')
    serializer_class = BairroSerializer

    def get_queryset(self):
        return self.queryset
