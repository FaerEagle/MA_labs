from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    token = models.CharField(max_length=30, null=True, verbose_name='token')