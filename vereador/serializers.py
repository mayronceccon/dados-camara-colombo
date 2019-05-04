from rest_framework import serializers
from .models import Vereador


class VereadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vereador
        exclude = ('cadastro', 'ativo',)
