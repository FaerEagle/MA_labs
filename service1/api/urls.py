from django.urls import path

from .views import sendAPIView, authenticate_APIView

urlpatterns = [
    path('service1/', sendAPIView),
    path('service1/auth/', authenticate_APIView)
]
