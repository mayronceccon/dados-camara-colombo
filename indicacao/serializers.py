from rest_framework import serializers
from pauta.serializers import PautaSerializer
from vereador.serializers import VereadorSerializer
from executor.serializers import ExecutorSerializer
from .models import Indicacao


class IndicacaoSerializer(serializers.ModelSerializer):
    pauta = PautaSerializer()
    vereador = VereadorSerializer()
    destinatario = ExecutorSerializer()

    class Meta:
        model = Indicacao
        fields = '__all__'
