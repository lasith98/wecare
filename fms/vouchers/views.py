import django.views.generic
from django.urls import reverse_lazy

# Create your views here.
from .models import Voucher


class VouchersListView(django.views.generic.ListView):
    model = Voucher
    template_name = "vouchers/view-vouchers-list.html"


class VouchersCreateView(django.views.generic.CreateView):
    model = Voucher
    template_name = "vouchers/new-voucher-form.html"
    success_url = reverse_lazy('vouchers:vouchers-list')
    fields = "__all__"


class VouchersUpdateView(django.views.generic.UpdateView):
    model = Voucher
    template_name = "vouchers/new-voucher-form.html"
    success_url = reverse_lazy('vouchers:vouchers-list')
    fields = "__all__"


class VouchersDeleteView(django.views.generic.DeleteView):
    model = Voucher
    template_name = ""
    success_url = reverse_lazy('vouchers:vouchers-list')
