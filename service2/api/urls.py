from django.urls import path

from .views import sendAPIView, authenticate_tokenAPIView

urlpatterns = [
    path('service2/', sendAPIView),
    path('service2/authenticate/', authenticate_tokenAPIView)
]