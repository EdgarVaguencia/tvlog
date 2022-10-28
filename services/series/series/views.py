from django.http import HttpResponse
from rest_framework import viewsets
from .models import serie
from .serializers import SerieSerializer
from .rabbit import send_test

def index (request):
    return HttpResponse('Hola mundo en las series')

def send_msg(request):
    msj = 'Hola a todos'

    if 'msj' in request.GET:
        msj = request.GET['msj']

    send_test(msj)

    return HttpResponse('Mandando mensajes')

class series_list(viewsets.ModelViewSet):
    queryset = serie.objects.all()
    serializer_class = SerieSerializer
