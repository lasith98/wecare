from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from collections import deque

class SalaryGroup(models.Model):
    sg_name = models.CharField(max_length=200,unique=True)
    sg_basic_salary = models.FloatField(null=False , validators=[MinValueValidator(0)])
    sg_hr_rate = models.FloatField(null=False , default= 0 , validators=[MinValueValidator(0)])
    sg_created_at = models.DateTimeField(auto_now_add=True)
    sg_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sg_name

class Employee(models.Model):
    emp_f_name = models.CharField(max_length=200,null=False)
    emp_s_name = models.CharField(max_length=200,null=False)
    emp_dob = models.DateField(null=False)
    emp_address_one = models.CharField(max_length=300)
    emp_address_two = models.CharField(max_length=300)
    emp_address_three = models.CharField(max_length=300)
    emp_nic = models.CharField(max_length=15 , null=False)
    emp_email = models.EmailField(max_length=200,unique=True,null=False)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now=True)
    sg_group = models.ForeignKey(SalaryGroup , null=False , on_delete=models.RESTRICT)

    def __str__(self):
        return self.emp_f_name

class DoctorSpecialization(models.Model):
    spe_title = models.CharField(max_length=200 , unique=True , null=False)

    def __str__(self):
        return self.spe_title

class Doctor(models.Model):
    emp_id = models.OneToOneField(Employee , null= False , on_delete=models.CASCADE)
    spe_id = models.ForeignKey(DoctorSpecialization , null=False , on_delete=models.RESTRICT)
    d_degree = models.CharField(max_length=200 , null=False)
    d_university = models.CharField(max_length=200 , null=False)
    d_moh_reg_number = models.CharField(max_length=20 , null=False , unique=True)
    d_max_patont_count = models.PositiveIntegerField(null=False , default=0 )

    def __str__(self):
        return self.emp_id.emp_f_name

class NursingOfficer(models.Model):
    from room_management_system import models as roomModel
    emp_id = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE)
    nf_maximum_qualification = models.CharField(max_length=300 , null=False)
    nf_is_assign = models.BooleanField(default=False)
    nf_moh_reg_number = models.CharField(max_length=20 , null=False , unique=True)
    r_id = models.ForeignKey(roomModel.Room ,blank=True , null=True, on_delete= models.RESTRICT)

    def __str__(self):
        return self.emp_id.emp_f_name

class HealthProfessionalsType(models.Model):
    hpt_title = models.CharField(max_length=300 , null= False)
    hpt_created_at = models.DateTimeField(auto_now_add=True)
    hpt_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hpt_title

class HealthProfessional(models.Model):
    emp_id = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE)
    hpt_id = models.ForeignKey(HealthProfessionalsType , null=False , on_delete=models.RESTRICT)
    hp_maximum_qualification = models.CharField(max_length=300 , null=False)

    def __str__(self):
        return self.emp_id.emp_f_name

class ManagementUnit(models.Model):
    mu_title = models.CharField(max_length=200 , null=False)
    mu_created_at = models.DateTimeField(auto_now_add=True)
    mu_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mu_title

class ManagementStaff(models.Model):
    emp_id = models.OneToOneField(Employee, null=False, on_delete=models.CASCADE)
    mu_id = models.ForeignKey(ManagementUnit , null=False , on_delete=models.RESTRICT)
    ms_designation = models.CharField(max_length=300 , null=False)

    def __str__(self):
        return self.emp_id.emp_f_name
