from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#all Users saved in the User database will follow this format and contain the following info
class User(AbstractUser):
    email = models.EmailField(unique=True, null=False) #pulling these methods from django docs on what types of fields will go for an email
    username = models.CharField(max_length=100)

    USERNAME_FIELD = "email" #emails will be same as username
    REQUIRED_FIELDS = ['username'] #a username must be provided, allows for email to be used as username when making superuser

    def __str__(self):
        return self.email