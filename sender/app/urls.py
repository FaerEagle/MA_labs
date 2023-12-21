from django.urls import path

from .views import sendmessage

urlpatterns = [
    path('send/', sendmessage),
]