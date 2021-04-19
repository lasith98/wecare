from django.db import models

# Create your models here.
class Items(models.Model):
    category = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    purchase = models.IntegerField()
    unitPrice = models.IntegerField()
    supplier = models.CharField(max_length=260)