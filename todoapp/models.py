from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guest(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class List(models.Model):
    guest = models.ForeignKey(Guest, null=True, on_delete=models.SET_NULL)
    task = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.task