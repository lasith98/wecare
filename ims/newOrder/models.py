from django.db import models

# Create your models here.
class NewOrder(models.Model):
    code = models.CharField(max_length=250)
    cusCategory = models.CharField(max_length=250)
    cusNo = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    unitPrice = models.IntegerField()
    amount = models.IntegerField()