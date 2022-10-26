from rest_framework import serializers
from .models import capitulo

class CapituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = capitulo
        fields = ['id', 'nombre']
