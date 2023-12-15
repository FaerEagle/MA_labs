from django.urls import path

from .views import sendAPIView

urlpatterns = [
    path('service2/', sendAPIView)
]