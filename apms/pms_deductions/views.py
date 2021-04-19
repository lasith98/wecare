from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


from .models import deduction
# Create your views here.

class deductionListView(ListView):
    model = deduction
    template_name = "pms/deduction-table.html"

class deductionCreateView(CreateView):
    model = deduction
    template_name = "pms/insert-deduction.html"
    success_url = reverse_lazy('pms_deductions:deduction-List')
    fields = '__all__'

class deductionUpdateView(UpdateView):
    model = deduction
    template_name = "pms/insert-deduction.html"
    success_url = reverse_lazy('pms_deductions:deduction-List')
    fields = '__all__'

class deductionDeleteView(DeleteView):
    model = deduction
    template_name = ""
    success_url = reverse_lazy('pms_deductions:deduction-List')