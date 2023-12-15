# from django.shortcuts import render
import pika
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

parameters = ('rabbitmq')

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='message_queue')
channel.basic_publish(exchange='', routing_key='message_queue', body='Hello, Service B!')
print(" [x] Sent 'Hello, Service B!'")
connection.close()