from django.urls import path

from .views import sendAPIView, authenticate_tokenAPIView

urlpatterns = [
    path('service2/', authenticate_tokenAPIView),
    path('service2/authenticate/', sendAPIView)
]