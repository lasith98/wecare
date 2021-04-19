from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

from .models import ams_client_leave_request

class leaveListView(ListView):
    model = ams_client_leave_request
    template_name = "ams/client/employee-request-list.html"

class leaveCreateView(CreateView):
    model = ams_client_leave_request
    template_name = "ams/client/employee-request-form.html"
    success_url = reverse_lazy('ams_client_leave_request:ams_client_leave_request-List')
    fields = ['employeeId','leaveDate','reason']

class leaveUpdateView(UpdateView):
    model = ams_client_leave_request
    template_name = "ams/client/employee-request-form.html"
    success_url = reverse_lazy('ams_client_leave_request:ams_client_leave_request-List')
    fields = ['employeeId','leaveDate','reason']

class leaveDeleteView(DeleteView):
    model = ams_client_leave_request
    success_url = reverse_lazy('ams_client_leave_request:ams_client_leave_request-List')