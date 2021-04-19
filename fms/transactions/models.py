from django.db import models


# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=10)
    date = models.DateTimeField()
    account_no = models.IntegerField()
    description = models.CharField(max_length=200)
    total_amount = models.FloatField()


