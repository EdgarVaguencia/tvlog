import json
import pika

connect = None

def open_connect():
    close_conect()

    connect = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))

    channel = connect.channel()

    return channel

def close_conect():
    if connect:
        connect.close()

def send_test(msj=''):
    channel = open_connect()

    channel.queue_declare(queue='hola')

    channel.basic_publish(exchange='', routing_key='hola', body=msj)

    print('Mensaje enviado')

    close_conect()

def share_serie(instance, tipo):
    channel = open_connect()

    channel.exchange_declare(exchange='brodcast_data', exchange_type='topic')

    data_json = {'id': instance.pk, 'nombre': instance.nombre}

    channel.basic_publish(exchange='brodcast_data', routing_key=tipo, body=json.dumps(data_json))
    print('Enviando: {} / {}'.format(tipo, data_json))

    close_conect()
