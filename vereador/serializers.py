from rest_framework import serializers
from .models import Vereador


class VereadorSerializer(serializers.ModelSerializer):
    projetos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    indicacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Vereador
        exclude = ('cadastro', 'ativo',)
