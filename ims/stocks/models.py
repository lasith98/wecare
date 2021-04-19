from django.db import models

# Create your models here.
class Stocks(models.Model):
    
    sCode = models.CharField(max_length=250)
    sDescription = models.CharField(max_length=250)
    sQuantity = models.IntegerField()
    sRStatus = models.CharField(max_length=250)