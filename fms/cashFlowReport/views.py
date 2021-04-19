import django.views.generic
from django.urls import reverse_lazy

# Create your views here.
from .models import CashFlowReport


class CashFlowListView(django.views.generic.ListView):
    model = CashFlowReport
    template_name = "cashFlowReport/cashFlow-list.html"


class CashFlowCreateView(django.views.generic.CreateView):
    model = CashFlowReport
    template_name = "cashFlowReport/cashFlow-form.html"
    success_url = reverse_lazy('cashFlowReport:cashFlow-list')
    fields = "__all__"


class CashFlowUpdateView(django.views.generic.UpdateView):
    model = CashFlowReport
    template_name = "cashFlowReport/cashFlow-form.html"
    success_url = reverse_lazy('cashFlowReport:cashFlow-list')
    fields = "__all__"


class CashFlowDeleteView(django.views.generic.DeleteView):
    model = CashFlowReport
    template_name = "cashFlowReport/cashFlow-list.html"
    success_url = reverse_lazy('cashFlowReport:cashFlow-list')
