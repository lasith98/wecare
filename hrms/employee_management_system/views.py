from django.contrib import messages
from django.db import transaction
from django.shortcuts import render , HttpResponse
from pip._internal import req

from room_management_system.models import Room

from . forms import *
# Create your views here.

def dashboard (request):


    doctors = Doctor.objects.all().count()
    nurses = NursingOfficer.objects.all().count()
    health_prof = HealthProfessional.objects.all().count()
    management_staff = ManagementStaff.objects.all().count()
    rooms = Room.objects.all().count()
    allocated_nurse = NursingOfficer.objects.filter(nf_is_assign = True).count
    unAllocated_nurse = NursingOfficer.objects.filter(nf_is_assign=False).count
    salary_group = SalaryGroup.objects.all().count

    context = {
        'doctor_count' : doctors,
        'nurse_count' : nurses,
        'health_prof' :health_prof,
        'management_staff' : management_staff,
        'rooms' : rooms,
        'allocated_nurse' : allocated_nurse,
        'unAllocated_nurse' : unAllocated_nurse,
        'salary_group' : salary_group,
    }


    return render(request , 'employee_management_system/ems_dashboard.html' , context)


#enrole a new doctor view
def enroll_new_doctor(request):

    #create form object
    employee_creation_form = Employee_creation_form(prefix='employee')
    doctor_creation_form = Doctor_creation_form(prefix='doctor')

    context = {
        'employee':employee_creation_form,
        'doctor' : doctor_creation_form
    }

    #check request is post or get
    if request.method == 'POST':
        emp_form = Employee_creation_form(request.POST , prefix='employee')
        doc_form = Doctor_creation_form(request.POST , prefix='doctor')

        #check if forms are valid
        if emp_form.is_valid() and doc_form.is_valid():
            try:
                with transaction.atomic():
                    emp = emp_form.save()
                    doc = doc_form.save(commit=False)
                    doc.emp_id = emp
                    doc.save()
                    #send message to front end
                    messages.success(request, 'Profile created success !')
            except:
                transaction.rollback()
        else:
            #attach error files in to the form
            emp_form.errors
            doc_form.errors
            context ['employee'] = emp_form
            context ['doctor'] = doc_form

            # send message to front end
            messages.warning(request, 'Profile was not created !')



    return render(request , 'employee_management_system/ems_enroll_new_doctor.html' , context)



#enrol new nursing officer
def enroll_new_nursing_officer(request):

    #create form object
    employee_creation_form = Employee_creation_form(prefix='employee')
    nurse_creation_form = Nurse_creation_form(prefix='nurse')

    context = {
        'employee' : employee_creation_form,
        'nurse' : nurse_creation_form,
    }

    if request.method == 'POST':
        emp_form = Employee_creation_form(request.POST , prefix='employee')
        nurse_form = Nurse_creation_form(request.POST , prefix='nurse')

        #check validation of form
        if emp_form.is_valid() and nurse_form.is_valid():

            try:
                with transaction.atomic():
                    emp = emp_form.save()
                    nurse = nurse_form.save(commit=False)
                    nurse.emp_id = emp
                    nurse.save()
                    #send message to front end
                    messages.success(request, 'Profile created success !')
            except:
                transaction.rollback()

        else:
            #attach error files in to the form
            emp_form.errors
            nurse_form.errors
            context['employee'] = emp_form
            context['nurse'] = nurse_form

            # send message to front end
            messages.warning(request, 'Profile was not created !')

    return  render(request , 'employee_management_system/ems_enrol_new_nursing_officer.html' , context)


#enrol new health proffesional
def enroll_new_health_professional(request):

    #create form object
    employee_creation_form = Employee_creation_form(prefix='employee')
    hprof_creation_form = Health_prof_creation_form(prefix='hprof')

    context = {
        'employee':employee_creation_form,
        'h_prof' : hprof_creation_form
    }

    if request.method == 'POST':
        emp_form = Employee_creation_form(request.POST , prefix='employee')
        hprof_form = Health_prof_creation_form(request.POST , prefix='hprof')

        if emp_form.is_valid() and hprof_form.is_valid():

            try:
                with transaction.atomic():
                    emp = emp_form.save()
                    hprof = hprof_form.save(commit=False)
                    hprof.emp_id = emp
                    hprof.save()
                    #send message to front end
                    messages.success(request, 'Profile created success !')
            except:
                transaction.rollback()


        else:
            #attach error files in to the form
            emp_form.errors
            hprof_form.errors
            context['employee'] = emp_form
            context['h_prof'] = hprof_form

            # send message to front end
            messages.warning(request, 'Profile was not created !')


    return render(request , 'employee_management_system/ems_enroll_new_health_professional.html' , context)


#enrol new management staff
def enroll_new_management_staff(request):

    #create form object
    employee_creation_form = Employee_creation_form(prefix='employee')
    management_staff_form = Management_saff_creation_form(prefix='staff')

    context = {
        'employee' : employee_creation_form,
        'staff' : management_staff_form,
    }

    if request.method == 'POST':
        emp_form = Employee_creation_form(request.POST , prefix='employee')
        staff_form = Management_saff_creation_form(request.POST , prefix='staff')

        #check validation of form
        if emp_form.is_valid() and staff_form.is_valid():

            try:
                with transaction.atomic():
                    emp = emp_form.save()
                    nurse = staff_form.save(commit=False)
                    nurse.emp_id = emp
                    nurse.save()
                    #send message to front end
                    messages.success(request, 'Profile created success !')
            except:
                transaction.rollback()

        else:
            #attach error files in to the form
            emp_form.errors
            staff_form.errors
            context['employee'] = emp_form
            context['nurse'] = staff_form

            # send message to front end
            messages.warning(request, 'Profile was not created !')

    return render(request , 'employee_management_system/ems_enroll_new_management_staff.html' , context)

#create new Salary group
def create_new_salary_group(request):

    s_group_form = Create_salary_group(prefix='salary_group')

    context = {
        's_group': s_group_form
    }

    if request.method == 'POST':
        salary_form = Create_salary_group(request.POST , prefix='salary_group')

        if salary_form.is_valid():
            salary_form.save()
            # send message to front end
            messages.success(request, 'Salary group created success !')
        else:
            salary_form.errors
            context['s_group'] = salary_form

            # send message to front end
            messages.warning(request, 'Salary group was not created !')

    return  render(request  , 'employee_management_system/ems_create_salary_group.html' , context)


#update salary group
def update_salary_group(request):

    salary_groups = SalaryGroup.objects.all()
    context = {
        'select_items' : salary_groups
    }

    #search request
    if request.method == 'POST' and 'search_form' in request.POST:
        salary_obj = SalaryGroup.objects.get(sg_name= request.POST.get('search_key'))
        sg_update_form = Create_salary_group(instance=salary_obj)
        context['salary_form'] = sg_update_form
        context['update_key'] = salary_obj.sg_name
        context['delete_key'] = salary_obj.sg_name

    #update request
    if request.method == 'POST' and 'update_form' in request.POST:

        salary_obj = SalaryGroup.objects.get(sg_name= request.POST.get('update_key'))
        update_s_group = Create_salary_group(request.POST , instance=salary_obj)

        if update_s_group.is_valid():
            update_s_group.save()
            # send message to front end
            messages.success(request, 'Salary group updated success !')
        else:
            update_s_group.errors
            context['salary_form'] = update_s_group
            context['update_key'] = request.POST.get('update_key')
            context['delete_key'] = request.POST.get('update_key')
            # send message to front end
            messages.warning(request, 'Salary group was not updated !')

    #delete request
    if request.method == 'POST' and 'delete_form' in request.POST:
        try:
            salart_delete_obj = SalaryGroup.objects.get(sg_name=request.POST.get('delete_key'))
            salart_delete_obj.delete()
            # send message to front end
            messages.success(request, 'Salary group deleted success !')
        except:
            # send message to front end
            messages.warning(request, 'Salary group was not deleted !')

    return render(request , 'employee_management_system/ems_update_salary_group.html' , context)

#create new Doctor Specialization
def new_doctor_specialization(request):

    d_spec_form = Create_doctor_specialization()
    context = {
        'd_spec' : d_spec_form
    }

    if request.method == 'POST' :
        d_spec_f = Create_doctor_specialization(request.POST)

        #check validation
        if d_spec_f.is_valid():
            d_spec_f.save()
            # send message to front end
            messages.success(request, 'Specialization created success !')

        else:
            d_spec_f.errors
            context['d_spec'] =d_spec_f
            # send message to front end
            messages.warning(request, 'Specialization was not created !')

    return render(request , 'employee_management_system/ems_new_doctor_specialization.html' ,context)

#update Specialization

def update_delete_specialization(request):

    spec_list = DoctorSpecialization.objects.all()

    context={
        'spec_list' : spec_list
    }

    #search request
    if request.method == 'POST' and 'search_form_spec' in request.POST:
        spec_obj = DoctorSpecialization.objects.get(id = request.POST.get('search_key'))
        spec_form = Create_doctor_specialization(instance=spec_obj)
        context['spec_form'] = spec_form
        context['update_key'] = request.POST.get('search_key')
        context['delete_key'] = request.POST.get('search_key')

    #update request
    if request.method == 'POST' and 'update_form_spec' in request.POST:
        spec_obj_update = DoctorSpecialization.objects.get(id=request.POST.get('update_key'))
        spec_form_req = Create_doctor_specialization(request.POST , instance = spec_obj_update)

        #check valiti
        if spec_form_req.is_valid():
            spec_form_req.save()
            # send message to front end
            messages.success(request, 'Specialization updated success !')

        else:
            spec_form_req.errors
            context['spec_list'] = spec_form_req
            context['update_key'] = request.POST.get('search_key')
            context['delete_key'] = request.POST.get('search_key')
            # send message to front end
            messages.warning(request, 'Specialization was not Updated !')

    #delete request
    if request.method == 'POST' and 'delete_form_spec' in request.POST:
        try:
            spec_delete_obj = DoctorSpecialization.objects.get(id=request.POST.get('delete_key_spec'))
            spec_delete_obj.delete()
            # send message to front end
            messages.success(request, 'Specialization deleted success !')
        except:
            # send message to front end
            messages.warning(request, 'Specialization was not deleted !')


    return render(request, 'employee_management_system/ems_update_delete_specialization.html' , context)


def doctor(request):

    doctors = Doctor.objects.all()

    context = {
        'doc' : doctors,
    }

    return render(request, 'employee_management_system/ems_doctor.html', context)

def nursing_officer(request):

    nurse = NursingOfficer.objects.all()

    context = {
        'nurse' :nurse,
    }

    return render(request, 'employee_management_system/ems_nursing_officer.html', context)

def health_prof(request):

    h_prof = HealthProfessional.objects.all()
    context = {
        'h_prof' :h_prof,
    }

    return render(request, 'employee_management_system/emp_health_professional.html', context)

def man_staff(request):

    man_staff = ManagementStaff.objects.all()

    context = {
        'man_staff' :man_staff,
    }

    return render(request, 'employee_management_system/ems_management_staff.html', context)


