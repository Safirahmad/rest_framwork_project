from django.db import models


class students(models.Model):
    name= models.CharField(max_length=30)
    roll_number=models.CharField(max_length=12)
    batch=models.CharField(max_length=20)

# Create your models here.
