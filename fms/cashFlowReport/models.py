from django.db import models

# Create your models here.


class CashFlowReport(models.Model):

    date = models.DateField()
    inflow_description = models.CharField(max_length=100)
    inflow_amount = models.IntegerField()
    outflow_description = models.CharField(max_length=100)
    outflow_amount = models.IntegerField()
