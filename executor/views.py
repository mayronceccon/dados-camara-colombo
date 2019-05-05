from django.shortcuts import render

from rest_framework import viewsets

from .models import Executor
from .serializers import ExecutorSerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all().order_by('nome')
    serializer_class = ExecutorSerializer
    http_method_names = ['get']
