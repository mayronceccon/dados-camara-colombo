from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Bairro

from .serializers import BairroSerializer


class BairroViewSet(viewsets.ViewSet):
    queryset = Bairro.objects.all()

    def get_queryset(self):
        return self.queryset

    def list(self, request):
        serializer = BairroSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = BairroSerializer(user)
        return Response(serializer.data)
