import django.views.generic
from django.urls import reverse_lazy

# Create your views here.
from .models import BalanceSheet


class BalanceSheetListView(django.views.generic.ListView):
    model = BalanceSheet
    template_name = "balanceSheet/balanceSheet-list.html"


class BalanceSheetCreateView(django.views.generic.CreateView):
    model = BalanceSheet
    template_name = "balanceSheet/balanceSheet-form.html"
    success_url = reverse_lazy('balanceSheet:balanceSheet-list')
    fields = "__all__"


class BalanceSheetUpdateView(django.views.generic.UpdateView):
    model = BalanceSheet
    template_name = "balanceSheet/balanceSheet-form.html"
    success_url = reverse_lazy('balanceSheet:balanceSheet-list')
    fields = "__all__"


class BalanceSheetDeleteView(django.views.generic.DeleteView):
    model = BalanceSheet
    template_name = "balanceSheet/balanceSheet-list.html"
    success_url = reverse_lazy('balanceSheet:balanceSheet-list')


