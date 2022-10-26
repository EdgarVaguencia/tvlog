from django.http import HttpResponse
from rest_framework import viewsets
from .models import serie
from .serializers import SerieSerializer

def index (request):
    return HttpResponse('Hola mundo en las series')

class series_list(viewsets.ModelViewSet):
    queryset = serie.objects.all()
    serializer_class = SerieSerializer
