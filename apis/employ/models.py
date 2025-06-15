from django.db import models

class employes(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=10)
# Create your models here.
