from django.db import models


# Create your models here.

class BalanceSheet(models.Model):

    year = models.DateField()
    assets = models.FloatField(null=True)
    liabilities = models.FloatField(null=True)
    equities = models.FloatField(null=True)
