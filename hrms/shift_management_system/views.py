from calendar import monthrange

from django.contrib import messages
from django.shortcuts import render
import math
import random

from django.db import transaction

from employee_management_system.models import NursingOfficer , HealthProfessional , ManagementStaff, Employee
from room_management_system.models import Room

from django.contrib.sessions.backends.db import SessionStore

from datetime import date

# Create your views here.
from . models import *

def genarate_next_month_shift(request):

    global contextx

    '''Handel Save Requests'''
    if request.method =="POST" and 'conform_save' in request.POST:

        try:
            with transaction.atomic():

                for nurse in  contextx['nursing']:
                    nurse.save()

                for h_prof in contextx['h_prof']:
                    h_prof.save()

                for man_staff in contextx['manage_staff']:
                    man_staff.save()

                # send message to front end
                messages.success(request, 'All Changers were Saved !')
        except:
            transaction.rollback()
            messages.warning(request, 'There Is An Error Please Try Again !')


    '''context'''
    contextx = {

    }



    '''Handel generate requests'''
    if request.method == 'POST' and 'generate' in request.POST:

        try:
            date = request.POST.get('month')
            month = date[5]+date[6]
            year = date[0]+date[1]+date[2]+date[3]

            month_key = {
                '01':'january',
                '02':'february',
                '03':'march',
                '04':'april',
                '05':'may',
                '06':'june',
                '07':'july',
                '08':'august',
                '09':'september',
                '10':'october',
                '11':'november',
                '12':'december',
            }

            all_shifts_in_year_month = Shift.objects.filter(s_year=year , s_month=month_key[month])

            if not all_shifts_in_year_month:

                data = {
                    'year' : year,
                    'month' : month,
                    'month_key' : month_key[month],
                }

                result = genarate_shift(data=data)


                contextx['nursing'] = result['nursing']
                contextx['h_prof'] = result['h_prof']
                contextx['manage_staff'] = result['manage_staff']

            else:
                messages.warning(request, 'There is an shift for this month')
        except:

            messages.warning(request, 'Some thing went wrong pleas try again! (check if there at least 2 nursing officers in room)')




    return render(request ,'shift_management_system/genarate_next_month_shift.html' , contextx)



def genarate_shift(data):

    '''For Nursing officer'''
    rooms = Room.objects.all()
    days_of_month = monthrange(int(data['year']), int(data['month']))[1]

    final_nurse_shift_list = []

    final_h_prof_shift_list = []

    final_manage_staff_list = []

    for room in rooms:

        nursing_officers = room.nursingofficer_set.all()
        n_count = nursing_officers.count()

        if n_count != 0:

            emp_working_time =  math.ceil(15 / n_count)

            for d in range (1 , days_of_month+1):
                date_to = data['year']+'-'+data['month']+'-'+str(d)

                start = 7
                global end
                end = 0

                for x in range(n_count):
                    end = 0
                    my_list = list(nursing_officers)
                    selected = random.sample(my_list , 2)

                    if (start + emp_working_time) >= 22 :
                        end = 22
                    else:
                        end += start+emp_working_time

                    for emp in selected:

                        emp1 = Shift(
                            s_year=data['year'],
                            s_date=date_to,
                            s_start=start,
                            s_end=end,
                            s_month=data['month_key'],
                            s_employee_shift = emp.emp_id
                        )

                        final_nurse_shift_list.append(emp1)

                    start += emp_working_time

    '''for Health professionals'''
    h_profs = HealthProfessional.objects.all()

    for h_prof in h_profs:

        for day in range(1 , days_of_month+1):
            date_to = data['year'] + '-' + data['month'] + '-' + str(day)

            emp = Shift(
                s_year=data['year'],
                s_date=date_to,
                s_start=7,
                s_end=18,
                s_month=data['month_key'],
                s_employee_shift=h_prof.emp_id
            )

            final_h_prof_shift_list.append(emp)


    '''For Management staffs'''
    man_staff = ManagementStaff.objects.all()

    for staff in man_staff:

        for day in range(1, days_of_month + 1):
            date_to = data['year'] + '-' + data['month'] + '-' + str(day)

            emp = Shift(
                s_year=data['year'],
                s_date=date_to,
                s_start=7,
                s_end=18,
                s_month=data['month_key'],
                s_employee_shift=staff.emp_id
            )

            final_manage_staff_list.append(emp)


    result = {
        'nursing' : final_nurse_shift_list,
        'h_prof' : final_h_prof_shift_list,
        'manage_staff' : final_manage_staff_list,

    }

    return result


def view_shifts(request):


    global contextView
    global shifts_by_month

    contextView = {

    }


    month_key = {
        '01': 'january',
        '02': 'february',
        '03': 'march',
        '04': 'april',
        '05': 'may',
        '06': 'june',
        '07': 'july',
        '08': 'august',
        '09': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december',
    }

    if request.method == 'POST' and 'search_by_month' in request.POST:
        date = request.POST.get('month')
        month = month_key[date[5] + date[6]]
        year = date[0] + date[1] + date[2] + date[3]

        shifts_by_month = Shift.objects.filter(s_year=year , s_month=month).order_by('s_employee_shift')

        if shifts_by_month:

            contextView = {
                'shifts' : shifts_by_month
            }

        else:
            messages.warning(request, 'There are no any shifts for this month')

    if request.method == 'POST' and 'search_by_emp' in request.POST:

        try:
            date = request.POST.get('month')
            month = month_key[date[5] + date[6]]
            year = date[0] + date[1] + date[2] + date[3]
            email = request.POST.get('email')

            emp = Employee.objects.get(emp_email = email)
            shifts_by_month = Shift.objects.filter(s_year=year , s_month=month , s_employee_shift = emp ).order_by('s_date')

            if shifts_by_month :

                contextView = {
                    'shifts' : shifts_by_month
                }

            else:
                messages.warning(request, 'There is no any shifts for this person')
        except:
            messages.warning(request, 'Some thing went wrong pleas try again!')

    if request.method == 'POST' and 'conform_delete' in request.POST:

        try:
            with transaction.atomic():
                for shift in shifts_by_month:
                    shift.delete()

            shifts_by_month = None
            messages.success(request, 'Shift Delete Success !')
        except:
            transaction.rollback()
            messages.warning(request, 'Some thing went wrong pleas try again!')


    employee = Employee.objects.all()
    contextView['employee_list'] = employee

    return render(request ,'shift_management_system/sms_view_shifts.html' ,contextView)


