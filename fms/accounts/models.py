from django.db import models

# Create your models here.

class Account(models.Model):

    acc_no = models.CharField(max_length=20)
    acc_name = models.CharField(max_length=50)
    date = models.DateField()
    bank_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    street_a1= models.CharField(max_length=100)
    street_a2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)



