from django.db import models

# Create your models here.

class deduction(models.Model):

    deduction_name = models.CharField(max_length=200)
    deduction_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.deduction_name

    class Meta:
        ordering = ['created_at']