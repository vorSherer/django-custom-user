from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    notes_field = models.CharField(max_length=60, default='')
    

    def __str__(self):
        return self.email
