from django.db import models


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    nic = models.CharField(max_length=10)
