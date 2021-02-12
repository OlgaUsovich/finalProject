from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=255)
    address = models.TextField('Адрес')

