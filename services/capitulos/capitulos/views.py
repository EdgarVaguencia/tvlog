from django.http import HttpResponse
from rest_framework import viewsets
from .models import capitulo
from .serializers import CapituloSerializer

def index (request):
    return HttpResponse('Hola mundo en las capitulos')

class capitulos_list(viewsets.ModelViewSet):
    queryset = capitulo.objects.all()
    serializer_class = CapituloSerializer
