from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

from .models import mark_attendance_manual

class attendanceList(ListView):
    model = mark_attendance_manual
    template_name = "ams/admin/attendance_list.html"

class attendanceCreateView(CreateView):
    model = mark_attendance_manual
    template_name = "ams/admin/mark_attendance.html"
    success_url = reverse_lazy('mark_attendance_manual:ams_admin_attendance_List')
    fields = ['employeeId']

class attendanceOutCreateView(UpdateView):
    model = mark_attendance_manual
    template_name = "ams/admin/mark_attendance.html"
    success_url = reverse_lazy('mark_attendance_manual:ams_admin_attendance_List')
    fields = ['outTime']





