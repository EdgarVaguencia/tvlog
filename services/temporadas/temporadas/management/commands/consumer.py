import json
import pika
from django.core.management.base import BaseCommand
from temporadas.models import serie

class Command(BaseCommand):
    def handle(self, *args, **options):
        connect = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

        channel_simple = connect.channel()
        channel_topic = connect.channel()

        channel_simple.queue_declare(queue='hola')
        channel_topic.exchange_declare(exchange='brodcast_data', exchange_type='topic')

        result_topic = channel_topic.queue_declare('', exclusive=True)
        queue_name = result_topic.method.queue
        channel_topic.queue_bind(exchange='brodcast_data', queue=queue_name, routing_key='serie.*')

        def callback_msg(ch, method, properties, body):
            print(body)

        def callback_serie(ch, method, properties, body):
            tipo = method.routing_key.split('.')[1]
            data = json.loads(body)

            if tipo == 'update':
                try:
                    view_serie = serie.objects.get(id_origen=data['id'])
                except serie.DoesNotExist:
                    view_serie = serie(id_origen=data['id'])
            else:
                view_serie = serie(
                    id_origen=data['id']
                )

            view_serie.nombre = data['nombre']
            view_serie.save()

        channel_simple.basic_consume(queue='hola', auto_ack=True, on_message_callback=callback_msg)
        channel_topic.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback_serie)

        print('A la espera de mensajes')
        channel_simple.start_consuming()
        channel_topic.start_consuming()
