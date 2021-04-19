from django.db import models

# Create your models here.
class Prscrpt(models.Model):
    medName = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=250)