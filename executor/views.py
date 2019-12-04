from rest_framework import viewsets
from rest_framework import mixins

from .models import Executor
from .serializers import ExecutorSerializer


class ExecutorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """Destinatários que são responsáveis pela execução das solicitações"""
    queryset = Executor.objects.all().order_by('nome')
    serializer_class = ExecutorSerializer

    def get_queryset(self):
        return self.queryset
