from django.db import models


# Create your models here.

class Report(models.Model):
    report_id = models.CharField(max_length=10)
    report_name = models.CharField(max_length=100)
    date_created = models.DateTimeField









