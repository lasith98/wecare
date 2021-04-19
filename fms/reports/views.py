import django.views.generic
from django.urls import reverse_lazy

# Create your views here.
from .models import Report
from django.views.generic import ListView, DeleteView


class ReportsListView(ListView):
    model = Report
    template_name = "reports/reports-list.html"





class ReportsDeleteView(DeleteView):
    model = Report
    template_name = "reports/reports-list.html"
    success_url = reverse_lazy('reports:reports-list')
