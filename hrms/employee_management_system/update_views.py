from django.contrib import messages
from django.db import transaction
from django.shortcuts import render , HttpResponse
from pip._internal import req

from . forms import *
# Create your views here.

#update doctor
def update_doctor(request):

    #add context data to later
    context = {

    }

    #handel search request
    if request.method == 'POST' and 'search_by_email' in request.POST:

        try:
            global doctor
            global employee
            employee = Employee.objects.get(emp_email=request.POST.get('d_email'))
            doctor = employee.doctor

            employee_update_form = Employee_creation_form(instance=employee , prefix= 'update_emp')
            doctor_update_form = Doctor_creation_form(instance=doctor , prefix= 'update_doc')

            context['emp_form'] = employee_update_form
            context['doc_form'] = doctor_update_form
            context['emp_id'] = employee.id

        except:
            # send message to front end
            messages.warning(request, 'There is no any doctor along this id')


    #handel update request
    if request.method == 'POST' and 'update_employee' in request.POST:

        emp_form = Employee_creation_form(request.POST ,instance=employee ,prefix='update_emp')
        doc_form = Doctor_creation_form(request.POST , instance=doctor,prefix='update_doc')

        if emp_form.is_valid() and doc_form.is_valid():
            emp_form.save()
            doc_form.save()
            # send message to front end
            messages.success(request, 'update success !')

        else:
            emp_form.errors
            doc_form.errors
            context['emp_form'] = emp_form
            context['doc_form'] = doc_form


            # send message to front end
            messages.warning(request, 'There is an error your updated data!')

    return render(request , 'employee_management_system/update/ems_update_doctor.html' , context)



#update nursing officer
def update_nurse(request):
    # add context data to later
    context = {

    }

    # handel search request
    if request.method == 'POST' and 'search_by_email' in request.POST:

        try:
            global nurse
            global employee
            employee = Employee.objects.get(emp_email=request.POST.get('d_email'))
            nurse = employee.nursingofficer

            employee_update_form = Employee_creation_form(instance=employee, prefix='update_emp')
            nurse_update_form = Nurse_creation_form(instance=nurse, prefix='update_nurse')

            context['emp_form'] = employee_update_form
            context['nurse_form'] = nurse_update_form
            context['emp_id'] = employee.id

        except:
            # send message to front end
            messages.warning(request, 'There is no any nurse along this email')

    # handel update request
    if request.method == 'POST' and 'update_employee' in request.POST:

        emp_form = Employee_creation_form(request.POST, instance=employee, prefix='update_emp')
        nurse_form = Nurse_creation_form(request.POST, instance=nurse, prefix='update_nurse')

        if emp_form.is_valid() and nurse_form.is_valid():
            emp_form.save()
            nurse_form.save()
            # send message to front end
            messages.success(request, 'update success !')

        else:
            emp_form.errors
            nurse_form.errors
            context['emp_form'] = emp_form
            context['nurse_form'] = nurse_form

            # send message to front end
            messages.warning(request, 'There is an error your updated data!')

    return render(request, 'employee_management_system/update/ems_update_nurse.html', context)



#update Health Professional
def update_health_prof(request):

    # add context data to later
    context = {

    }

    # handel search request
    if request.method == 'POST' and 'search_by_email' in request.POST:

        try:
            global health_prof
            global employee
            employee = Employee.objects.get(emp_email=request.POST.get('d_email'))
            health_prof = employee.healthprofessional

            employee_update_form = Employee_creation_form(instance=employee, prefix='update_emp')
            health_prof_update_form = Health_prof_creation_form(instance=health_prof, prefix='update_h_prof')

            context['emp_form'] = employee_update_form
            context['h_prof_form'] = health_prof_update_form
            context['emp_id'] = employee.id

        except:
            # send message to front end
            messages.warning(request, 'There is no any health professional along this email')



    # handel update request
    if request.method == 'POST' and 'update_employee' in request.POST:

        emp_form = Employee_creation_form(request.POST, instance=employee, prefix='update_emp')
        health_prof_form = Health_prof_creation_form(request.POST, instance=health_prof, prefix='update_h_prof')

        if emp_form.is_valid() and health_prof_form.is_valid():
            emp_form.save()
            health_prof_form.save()
            # send message to front end
            messages.success(request, 'update success !')

        else:
            emp_form.errors
            health_prof_form.errors
            context['emp_form'] = emp_form
            context['h_prof_form'] = health_prof_form

            # send message to front end
            messages.warning(request, 'There is an error your updated data!')

    return render(request ,'employee_management_system/update/ems_update_health_professional.html' , context)



#update management staff
def update_management_staff(request):

    # add context data to later
    context = {

    }

    # handel search request
    if request.method == 'POST' and 'search_by_email' in request.POST:

        try:
            global man_staff
            global employee
            employee = Employee.objects.get(emp_email=request.POST.get('d_email'))
            man_staff = employee.managementstaff

            employee_update_form = Employee_creation_form(instance=employee, prefix='update_emp')
            man_staff_update_form = Management_saff_creation_form(instance=man_staff, prefix='man_staff')

            context['emp_form'] = employee_update_form
            context['man_staff'] = man_staff_update_form
            context['emp_id'] = employee.id

        except:
            # send message to front end
            messages.warning(request, 'There is no any management staff along this email')


    # handel update request
    if request.method == 'POST' and 'update_employee' in request.POST:

        emp_form = Employee_creation_form(request.POST, instance=employee, prefix='update_emp')
        man_update_form = Management_saff_creation_form(request.POST, instance=man_staff, prefix='man_staff')

        if emp_form.is_valid() and man_update_form.is_valid():
            emp_form.save()
            man_update_form.save()
            # send message to front end
            messages.success(request, 'update success !')

        else:
            emp_form.errors
            man_update_form.errors
            context['emp_form'] = emp_form
            context['man_staff'] = man_update_form

            # send message to front end
            messages.warning(request, 'There is an error your updated data!')


    return render(request ,'employee_management_system/update/ems_update_management_staff.html' , context)