import random
from time import sleep

import requests
from requests.adapters import HTTPAdapter, Retry
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *

@api_view(['GET'])
def sendAPIView(request):

    return Response({"Это сервис номер 1"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def authenticate_APIView(request):   # получения, создание и отправка кода

    login = request.data.get('login')
    password = request.data.get('password') #в скобках это как поля в заросе должны называться

    profile_queryset = UserProfile.objects.filter(login=login)  #Profile это как у тебя модель с пользователем и токеном называться будет. Можешь хоть как назвать.

    if profile_queryset.exists():
        profile = profile_queryset[0]
        if profile.password == password:
            chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#$%^&*.'
            token_list = []
            for i in range(30):
                token_list.append(random.choice(chars))

            token = ''.join(token_list)

            profile.token = token
            profile.save()

            params = {
                "token": token,
            }

            endpoint = "http://service2:8001/service2/"
            response = None
            while response is None:
                try:
                    response = requests.post(
                        endpoint, data=params)  #надо подумать что с ответом делать
                    break
                except Exception as error:
                    print("Ошибка аунтентификации, причина: ", error)
                    sleep(1.5)
                    continue
            # response = requests.post(
            #          endpoint, params=params, headers=headers).json()  #надо подумать что с ответом делать
            return Response({'token': token}, status=status.HTTP_200_OK)

    return Response({'error': 'Неверные данные', }, status=status.HTTP_400_BAD_REQUEST)
