from django import forms
from django.forms.models import ModelForm
from . models import *

class Employee_creation_form(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_f_name': 'First Name',
            'emp_s_name' : 'Second Name',
            'emp_dob' : 'Date Of Birth (MM/DD/YYYY)',
            'emp_address_one' : 'Address One',
            'emp_address_two': 'Address Two',
            'emp_address_three' : 'Address Three',
            'emp_nic' : 'NIC',
            'emp_email' : 'Email Address',
            'sg_group' : 'Salary Group',
        }
        error_messages = {
            'emp_email' : {
                'unique' : 'This email address is already exist',
            }
        }

class Doctor_creation_form(ModelForm):

    class Meta:
        model = Doctor
        exclude = {'emp_id'}
        labels = {
            'spe_id' : 'Doctor Specialization',
            'd_degree' : 'Degree',
            'd_university' : 'University',
            'd_moh_reg_number' : 'MOH Registration Number',
            'd_max_patont_count' : 'Maximum Patients Count'
        }

        error_messages = {
            'd_moh_reg_number' : {
                'unique' : 'This doctor is already exist',
            }
        }

class Nurse_creation_form(ModelForm):

    class Meta:
        model = NursingOfficer
        exclude = {'emp_id' , 'nf_is_assign' , 'r_id'}
        labels = {
            'nf_maximum_qualification' : 'Maximum Qualification',
            'nf_moh_reg_number' : 'Nursing Officer Registration Number'
        }

class Health_prof_creation_form(ModelForm):

    class Meta:
        model = HealthProfessional
        exclude = {'emp_id'}
        labels = {
            'hp_maximum_qualification' : 'Maximum Qualification',
            'hpt_id' : 'Health Professionals Type'
        }

class Management_saff_creation_form(ModelForm):

    class Meta:
        model = ManagementStaff
        exclude = {'emp_id'}
        labels = {
            'mu_id' : 'Management Unit',
            'ms_designation' : 'Designation'
        }

class Create_salary_group(ModelForm):
    class Meta:
        model = SalaryGroup
        fields = '__all__'
        labels = {
            'sg_name' : 'Salary Group Name',
            'sg_basic_salary' : 'Basic Salary',
            'sg_hr_rate' : 'Hourly Rate For The Employee'
        }

class Create_doctor_specialization(ModelForm):
    class Meta:
        model = DoctorSpecialization
        fields = '__all__'
        labels = {
            'spe_title' : 'Specialization title'
        }
        error_messages = {
            'spe_title' : {
                'unique' : 'This specialization is already exist',
            }
        }
