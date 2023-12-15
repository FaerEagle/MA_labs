# from django.shortcuts import render
import pika

def callback(body):
    print(f" [x] Received {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='message_queue')

channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
