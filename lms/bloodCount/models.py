from django.db import models

# Create your models here.
class BloodCount(models.Model):
    tstBox1 = models.CharField(max_length=250)
    tstBox2 = models.CharField(max_length=250)
    tstBox3 = models.CharField(max_length=250)
    tstBox4 = models.CharField(max_length=250)
    resultBox1 = models.CharField(max_length=250)
    resultBox2 = models.CharField(max_length=250)
    resultBox3 = models.CharField(max_length=250)
    resultBox4 = models.CharField(max_length=250)
    normalBox1 = models.CharField(max_length=250)
    normalBox2 = models.CharField(max_length=250)
    normalBox3 = models.CharField(max_length=250)
    normalBox4 = models.CharField(max_length=250)
    age = models.IntegerField()
    date = models.DateField()