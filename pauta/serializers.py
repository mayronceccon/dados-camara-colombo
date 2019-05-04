from rest_framework import serializers
from .models import Pauta


class PautaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pauta
        exclude = ('cadastro', 'indicacao_exportada',)
