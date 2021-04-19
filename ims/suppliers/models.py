from django.db import models

# Create your models here.
class Suppliers(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.EmailField()
    date = models.DateField()