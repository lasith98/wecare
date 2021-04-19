from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.IntegerField()

