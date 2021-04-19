# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from billing.models import Billing


# Create your views here.


class BillingListView(ListView):
    model = Billing
    template_name = "billing/billing-list.html"


class BillingCreateView(CreateView):
    model = Billing
    template_name = "billing/billing-form.html"
    success_url = reverse_lazy('billing:billing-list')
    fields = "__all__"


class BillingUpdateView(UpdateView):
    model = Billing
    template_name = "billing/billing-form.html"
    success_url = reverse_lazy('billing:billing-list')
    fields = "__all__"


class BillingDeleteView(DeleteView):
    model = Billing
    template_name = ""
    success_url = reverse_lazy('billing:billing-list')

# Create your views here.
