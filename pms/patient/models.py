import datetime

from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from choices.BloodGroupChoice import BloodGroupChoice
from util.util import calculate_age


class Guardian(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=250)
    address = models.TextField()


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nic = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=250)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5, choices=BloodGroupChoice.choices, default=BloodGroupChoice.NA)
    address = models.TextField()
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def age(self):
        return calculate_age(self.dob)
