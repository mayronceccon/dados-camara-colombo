from rest_framework import serializers
from .models import Vereador


class VereadorSerializer(serializers.ModelSerializer):
    projetos = serializers.SerializerMethodField()
    indicacoes = serializers.SerializerMethodField()
    legislaturas = serializers.SerializerMethodField()

    class Meta:
        model = Vereador
        exclude = ('cadastro', 'ativo',)

    def get_projetos(self, obj):
        return obj.projetos.count()

    def get_indicacoes(self, obj):
        return obj.indicacoes.count()

    def get_legislaturas(self, obj):
        return len(obj.legislaturas)
