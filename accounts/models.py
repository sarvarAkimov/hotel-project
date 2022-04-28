from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class People(AbstractUser):
    email = models.EmailField(max_length=155)
