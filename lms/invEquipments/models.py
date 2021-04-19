from django.db import models

# Create your models here.
class InvEquipments(models.Model):
    code = models.CharField(max_length=250)
    quantity = models.IntegerField()
