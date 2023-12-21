# from django.shortcuts import render
import pika
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

parameters = pika.URLParameters(
    'amqps://qhnsgzra:EHtEptokheMchKCbWhlRMifrz-ZTyKJ3@woodpecker.rmq.cloudamqp.com/qhnsgzra')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()


@api_view(['GET'])
def sendmessage(request):
    channel.queue_declare(queue='message_queue')
    channel.basic_publish(exchange='', routing_key='message_queue', body="Message from sender")
    # return Response({"message": request.data}, status=status.HTTP_200_OK)
    return Response({"Сообщение отправлено"}, status=status.HTTP_200_OK)

# connection.close()
