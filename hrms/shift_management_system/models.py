from django.db import models

# Create your models here.

class Shift(models.Model):

    months = (
        ('january','January'),
        ('february','Jebruary'),
        ('march','March'),
        ('april','April'),
        ('may','May'),
        ('june','June'),
        ('july','July'),
        ('august','August'),
        ('september','September'),
        ('october','October'),
        ('november','November'),
        ('december','December')
    )

    from employee_management_system.models import Employee
    s_year = models.CharField(max_length=4 , null=True)
    s_date = models.DateField(null=False)
    s_start = models.IntegerField(null=False)
    s_end = models.IntegerField(null=False)
    s_month = models.CharField(choices= months , max_length= 200 , null=True)
    s_employee_shift = models.ForeignKey(Employee, on_delete=models.DO_NOTHING , default=None)