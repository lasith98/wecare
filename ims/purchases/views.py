from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from purchases.models import Purchases
from stocks.models import Stocks


class PurchasesListView(ListView):
    model = Purchases
    template_name = "purchases/purchases-list.html"


class PurchasesCreateView(CreateView):
    model = Purchases
    template_name = "purchases/purchases-form.html"
    success_url = reverse_lazy('purchases:purchases-list')
    fields = "__all__" 
    


class PurchasesUpdateView(UpdateView):
    model = Purchases
    template_name = "purchases/purchases-form.html"
    success_url = reverse_lazy('purchases:purchases-list')
    fields = "__all__"


class PurchasesDeleteView(DeleteView):
    model = Purchases
    template_name = ""
    success_url = reverse_lazy('purchases:purchases-list')
