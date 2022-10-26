from django.http import HttpResponse
from rest_framework import viewsets
from .models import temporada
from .serializers import TemporadaSerializer

def index (request):
    return HttpResponse('Hola mundo en las temporadas')

class temporadas_list(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
