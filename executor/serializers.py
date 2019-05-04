from rest_framework import serializers
from .models import Executor


class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = '__all__'
