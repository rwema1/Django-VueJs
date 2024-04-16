from django.db import models
from django.contrib.auth.models import AbstractUser

#USER MODEL
class User(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=200)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name