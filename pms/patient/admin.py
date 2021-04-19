from django.contrib import admin

# Register your models here.
from patient.models import Guardian, Patient

admin.site.register(Guardian)
admin.site.register(Patient)
