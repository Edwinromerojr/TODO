from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class List(models.Model):
    task = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.task