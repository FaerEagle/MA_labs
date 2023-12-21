# from django.shortcuts import render
import pika


def callback(ch, method, properties, body):
    print(f"Получено сообщение: {body}")


parameters = pika.URLParameters('amqps://qhnsgzra:EHtEptokheMchKCbWhlRMifrz-ZTyKJ3@woodpecker.rmq.cloudamqp.com/qhnsgzra')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='message_queue')

channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)

print('Ожидание сообщений...')
channel.start_consuming()
