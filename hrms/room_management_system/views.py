from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render , HttpResponse , redirect

from . forms import *

# Create your views here.
from employee_management_system.models import Employee

from employee_management_system.models import NursingOfficer


def add_room(request):

    room_create_form = Room_creation_form

    context = {
        'room_form' : room_create_form
    }

    #handel post request
    if request.method == 'POST' and 'add_room' in request.POST:

        room_form = room_create_form(request.POST)

        if room_form.is_valid():
            room_form.save()
            # send message to front end
            messages.success(request, 'Room was added successfully!')
        else:
            room_form.errors
            context['room_form'] = room_form
            # send message to front end
            messages.warning(request, 'Room was not Added!')

    return render(request , 'room_management_system/insert/rms_add_room.html' , context)



def update_room(request):

    context = {

    }

    global room

    #handel room search request
    if request.method == 'POST' and 'search_room_by_name' in request.POST:

        try:
            room = Room.objects.get(r_name=request.POST.get('r_name'))
            room_update_form = Room_creation_form(instance=room)
            context['room_update_form'] = room_update_form
            context['room_id'] = room.id

        except:
            messages.warning(request, 'Room Name Is Incorrect !')


    #handel update request
    if request.method == 'POST' and 'update_room' in request.POST:

        update_from = Room_creation_form(request.POST , instance=room)

        if update_from.is_valid():
            update_from.save()
            messages.success(request, 'Room was updated successfully!')
        else:
            update_from.errors
            context['room_update_form'] = update_from
            messages.warning(request, 'Room update failed !')

    return render(request , 'room_management_system/update/rms_update_room.html' , context)


def delete_room(request):

    context = {

    }

    #handel room search request
    if request.method == 'POST' and 'search_room_by_name' in request.POST:

        try:
            room = Room.objects.get(r_name=request.POST.get('r_name'))
            context['room_name'] = room.r_name
            context['room_size'] = room.r_size
            context['room_location'] = room.r_location
            context['room_id'] = room.id

        except:
            messages.warning(request, 'Room Name Is Incorrect !')

    #delete request
    if request.method == "POST" and 'delete_room' in request.POST:
        try:
            room = Room.objects.get(id=request.POST.get('r_id'))
            room.delete()
            messages.success(request, 'Room was deleted successfully!')

        except:
            messages.warning(request, 'Room Name Is Incorrect !')

    return render(request , 'room_management_system/delete/rms_delete_room.html' , context)



def room_list(request):

    room_list = Room.objects.all().order_by('-r_created_at')

    context= {
        'room_list' : room_list,
    }

    return render(request , 'room_management_system/view/rms_room_list.html' , context)


#allocate doctor to the hospital

def allocate_doc_r(request):

    context ={

    }

    #get all rooms in selected day
    if request.method == 'POST' and 'search_by_day' in request.POST:

        rooms = AllocationTable.objects.filter(at_day=request.POST.get('day'))

        #add day to the context
        context['day'] = request.POST.get('day')

        allocation_vector = {
            '7-10': {
                'time' : '7-10',
                'available' : True,
            },
            '10-13':{
                'time': '10-13',
                'available': True,
            },
            '13-16':{
                'time': '13-16',
                'available': True,
            },
            '16-19':{
                'time': '16-19',
                'available': True,
            },
            '19-22':{
                'time': '19-22',
                'available': True,
            }
        }

        if not rooms:
            #no any result
            room_list = Room.objects.all()
            room_vector = {

            }

            #check if there is any room
            if room_list:

                for room in room_list:

                    room_vector[room.r_name] = {
                        'room' : room,
                        'allocate_vector' : allocation_vector
                    }
                context['room_vector'] = room_vector

            else:
                messages.warning(request, 'No any rooms registered yet !')

        else:
            #alredy time slots are requested to rooms
            room_list = Room.objects.all()



            room_vector = {

            }

            if room_list:



                for r in room_list:

                    t_table = {
                        '7-10': {
                            'time': '7-10',
                            'available': True,
                        },
                        '10-13': {
                            'time': '10-13',
                            'available': True,
                        },
                        '13-16': {
                            'time': '13-16',
                            'available': True,
                        },
                        '16-19': {
                            'time': '16-19',
                            'available': True,
                        },
                        '19-22': {
                            'time': '19-22',
                            'available': True,
                        }
                    }

                    for allocation in rooms:

                        if allocation.r_id.id == r.id:

                            dict = {
                                'time': allocation.at_slot,
                                'available': False,
                            }

                            t_table[allocation.at_slot] = dict


                        room_vector[r.r_name]={
                            'room' : r,
                            'allocate_vector' : t_table
                        }

                context['room_vector'] = room_vector


            else:
                messages.warning(request, 'No any rooms registered yet ! 2')

    return render(request , 'room_management_system/insert/rms_allocate_d_room.html' , context)


def allocate_room(request):

    if request.method == 'POST' and 'check_time_slot' in request.POST:

        try:
            employee = Employee.objects.get(emp_email=request.POST.get('doc_email'))
            doc = employee.doctor

            #allocate room
            try:
                time_slots = request.POST.getlist('time_slot')

                if time_slots:
                    day = request.POST.get('day')
                    r_id = request.POST.get('room_id')
                    room = Room.objects.get(id=r_id)
                    try:

                        for time in time_slots:
                            #save time slots
                            allocation_unit = AllocationTable.objects.create(at_day=day , at_slot=time , d_id=doc , r_id = room )
                            allocation_unit.save()

                        messages.success(request, 'Allocation success')

                    except:
                        messages.warning(request, 'Some thing went wrong pleas try again! 1')

                else:
                    messages.warning(request, 'No any room checked')

            except:
                messages.warning(request, 'No any room checked')

        except:
            messages.warning(request, 'There is no any doctor with this email')
    else:
        messages.warning(request, 'Some thing went wrong pleas try again!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def allocate_nurses(request):

    rooms = Room.objects.all()

    context = {
        'rooms' : rooms,
    }

    '''
        handel search requests
    '''
    if request.method == 'POST' and 'search_room' in request.POST:



        room = Room.objects.get(id=request.POST.get('selected_room'))

        nurses = NursingOfficer.objects.filter(nf_is_assign= False)

        allocated_nurses = room.nursingofficer_set.all()

        context['selected_room'] = room
        context['available_nurses'] = nurses
        context['allocated_nuress'] = allocated_nurses


    '''
        handel update requests
    '''
    if request.method == 'POST' and 'update_allocation' in request.POST:

        elected_room = request.POST.get('room_to_allocate')
        elect_to_allocate = request.POST.getlist('allocated')
        elect_to_unAllocate = request.POST.getlist('unAllocated')

        try:

            elected_room = Room.objects.get(id = elected_room)

            for element in elect_to_allocate:
                nurse = NursingOfficer.objects.get(id = element)
                nurse.nf_is_assign = True
                nurse.r_id_id = elected_room
                nurse.save()

            for element in elect_to_unAllocate:
                nurse = NursingOfficer.objects.get(id = element)
                nurse.nf_is_assign = False
                nurse.r_id_id = None
                nurse.save()

            messages.success(request, 'Room : '+elected_room.r_name+', Allocation Success!')
        except:
            messages.warning(request, 'Some thing went wrong pleas try again!')


    return render(request ,'room_management_system/insert/rms_allocate_nurses.html' ,context)
