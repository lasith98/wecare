from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
from .models import allowance

class allowanceListView(ListView):
    model = allowance
    template_name = "pms/increment-table.html"

class allowanceCreateView(CreateView):
    model = allowance
    template_name ="pms/insert-increment.html"
    fields = ['increment_name', 'increment_amount']
    success_url = reverse_lazy('pms_allowances:allowance-List')


class allowanceUpdateView(UpdateView):
    model = allowance
    template_name = "pms/insert-increment.html"
    fields = ['increment_name', 'increment_amount']
    success_url = reverse_lazy('pms_allowances:allowance-List')


class allowanceDeleteView(DeleteView):
    model = allowance
    template_name = ""
    success_url = reverse_lazy('pms_allowances:allowance-List')



