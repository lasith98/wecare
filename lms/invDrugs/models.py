from django.db import models

# Create your models here.
class InvDrugs(models.Model):
    code = models.CharField(max_length=250)
    quantity = models.IntegerField()
