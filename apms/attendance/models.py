from django.db import models

# Create your models here.

class mark_attendance_manual(models.Model):

    employeeId = models.CharField(max_length=20)
    inTime = models.DateTimeField(auto_now_add=True)
    outTime = models.DateTimeField( blank= True , null= True)


