import os
import json
import pika
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capitulos.settings')
django.setup()
from capitulos.models import temporada

connect = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

channel_topic = connect.channel()

channel_topic.exchange_declare(exchange='brodcast_data', exchange_type='topic')

result_topic = channel_topic.queue_declare('', exclusive=True)
queue_name = result_topic.method.queue
channel_topic.queue_bind(exchange='brodcast_data', queue=queue_name, routing_key='temporada.*')
channel_topic.queue_bind(exchange='brodcast_data', queue=queue_name, routing_key='serie.update')

def callback(ch, method, properties, body):
    model = method.routing_key.split('.')[0]
    tipo = method.routing_key.split('.')[1]

    if model == 'temporada':
        temporada_function(tipo, body)
    elif model == 'serie':
        serie_function(tipo, body)

def temporada_function(tipo, body):
    data = json.loads(body)
    if tipo == 'update':
        try:
            view_temporada = temporada.objects.get(pk=data['id'])
        except temporada.DoesNotExist:
            view_temporada = temporada()
    else:
        view_temporada = temporada(
            pk=data['id']
        )

    view_temporada.nombre = data['nombre']
    view_temporada.serie = data['serie']
    view_temporada.serie_id = data['serie_id']
    view_temporada.save()

def serie_function(tipo, body):
    data = json.loads(body)
    for v_temporada in temporada.objects.filter(serie_id=data['id']):
        v_temporada.serie = data['nombre']
        v_temporada.save()

channel_topic.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

print('A la espera de mensajes')
channel_topic.start_consuming()
