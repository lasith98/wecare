from django.db import models

# Create your models here.

class ams_client_leave_request(models.Model):
    employeeId = models.CharField(max_length=50)
    leaveDate = models.DateField()
    reason = models.CharField(max_length=1000, null=True)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ['created_at']


