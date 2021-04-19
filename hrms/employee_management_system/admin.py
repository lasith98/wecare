from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(SalaryGroup)
admin.site.register(DoctorSpecialization)
admin.site.register(Doctor)
admin.site.register(NursingOfficer)
admin.site.register(HealthProfessionalsType)
admin.site.register(HealthProfessional)
admin.site.register(ManagementUnit)
admin.site.register(ManagementStaff)

