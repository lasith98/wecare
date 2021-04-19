from django.db import models

# Create your models here.
class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    quantity = models.IntegerField()
    date_value = models.CharField(max_length=45)
