from time import sleep

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

@api_view(['GET'])
def sendAPIView(request):
    return Response({"Это сервис номер 2"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def authenticate_tokenAPIView(request):   # обработка кода
    token = request.data.get('token')

    token_queryset = UserProfile.objects.filter(token=token)  #Profile это как у тебя модель с пользователем и токеном называться будет. Можешь хоть как назвать.

    if token_queryset.exists():
        profile = token_queryset[0]
        if profile.token == token:
            return Response({'response': 'Доступ получен'}, status=status.HTTP_200_OK)

    return Response({'error': 'Неверные данные, в доступе отказано', }, status=status.HTTP_400_BAD_REQUEST)
