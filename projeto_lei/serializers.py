from rest_framework import serializers
from vereador.serializers import VereadorSerializer

from .models import ProjetoLei


class ProjetoLeiSerializer(serializers.ModelSerializer):
    vereador = VereadorSerializer()

    class Meta:
        model = ProjetoLei
        exclude = ('observacao', )
