from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from .models import attendance_chart

class attendanceChartView(TemplateView):
    model = attendance_chart;
    template_name = "ams/admin/attendance_tracker.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["quierySet"] = attendance_chart.objects.all()
        return context