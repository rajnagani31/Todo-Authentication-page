from django.db import models

# Create your models here.

class formregister(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=255,unique=True)
    password=models.CharField(max_length=100)



    