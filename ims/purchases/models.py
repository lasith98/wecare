from django.db import models

# Create your models here.
class Purchases(models.Model):
    pDate = models.DateField()
    pInvoice = models.CharField(max_length=250)
    pCode = models.CharField(max_length=250)
    pDescription = models.CharField(max_length=250)
    pQuantity = models.IntegerField()