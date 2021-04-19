from django import forms
from django.forms.models import ModelForm
from . models import *

class Room_creation_form(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        labels = {
            'r_name' : 'Room Name',
            'r_size' : 'Room Size',
            'r_location' : 'Room Location'
        }
        error_messages = {
            'r_name' : {
                'unique' : 'This room is already exist',
            }
        }