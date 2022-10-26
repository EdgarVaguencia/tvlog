from rest_framework import serializers
from .models import serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = serie
        fields = ['id', 'nombre']
