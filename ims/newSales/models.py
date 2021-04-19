from django.db import models

# Create your models here.
class NewSales(models.Model):
    code = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    RStatus = models.CharField(max_length=250)