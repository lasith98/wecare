from django.db import models

# Create your models here.

class attendance_chart(models.Model):
    month = models.DateField()
    quantity = models.IntegerField()
