from django.db import models

# Create your models here.

class allowance(models.Model):      #creating allowance model

    #increment id will be automatically  generated

    increment_name = models.CharField(max_length=200)           #name of the increment
    increment_amount = models.FloatField()                      #amount of the increment
    date_created = models.DateTimeField(auto_now_add=True)      #date that record added to database(Auomatically added to DB)

    def __str__(self):
        return self.increment_name

    class Meta:
        ordering = ['date_created']
