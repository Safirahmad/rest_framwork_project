from django.db import models

class hr(models.Model):
    hr_name=models.CharField(max_length=20)
    hr_email=models.CharField(max_length=30)
    
# Create your models here.
