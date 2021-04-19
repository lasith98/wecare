from django.db import models
from employee_management_system import models as empModel

# Create your models here.


class Room(models.Model):
    r_name = models.CharField(max_length=200 , unique=True)
    r_size = models.FloatField(null=False)
    r_location = models.CharField(max_length=350 , null=False)
    r_created_at = models.DateTimeField(auto_now_add=True)
    r_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.r_name

class AllocationTable(models.Model):

    class Meta:
        unique_together = (('at_day', 'at_slot' , 'r_id'),)

    days = (
        ('monday' , 'Monday'),
        ('tuesday' , 'Tuesday'),
        ('wednesday' , 'Wednesday'),
        ('thursday' , 'Thursday'),
        ('friday', 'Friday'),
        ('saturday' , 'Saturday'),
        ('sunday' , 'Sunday'),
    )
    at_day = models.CharField(max_length=30 , choices=days , null=False)
    at_slot = models.CharField(max_length=15 , null=False)
    r_id = models.ForeignKey(Room , null=False , on_delete=models.RESTRICT)
    d_id = models.ForeignKey(empModel.Doctor, null=False ,on_delete=models.CASCADE)

    def __str__(self):
        name = self.at_day+ " "+ self.r_id.r_name+ " " + self.at_slot + " " +self.d_id.emp_id.emp_f_name
        return name
