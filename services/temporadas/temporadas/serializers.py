from rest_framework import serializers
from .models import temporada

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = temporada
        fields = ['id', 'nombre']
