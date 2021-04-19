from django.db import models


# Create your models here.

class Voucher(models.Model):
    voucher_no = models.IntegerField()
    date = models.DateField()
    account_no = models.IntegerField()
    supplier_id = models.CharField(max_length=250)
    description = models.CharField(max_length=200)
    total_amount = models.FloatField()
