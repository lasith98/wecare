from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from suppliers.models import Suppliers


class SuppliersListView(ListView):
    model = Suppliers
    template_name = "suppliers/suppliers-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Suppliers.objects.filter(Q(code =query))
            return object_list
        else:
            object_list = Suppliers.objects.all()
            return object_list

class SuppliersCreateView(CreateView):
    model = Suppliers
    template_name = "suppliers/suppliers-form.html"
    success_url = reverse_lazy('suppliers:suppliers-list')
    fields = "__all__"


class SuppliersUpdateView(UpdateView):
    model = Suppliers
    template_name = "suppliers/suppliers-form.html"
    success_url = reverse_lazy('suppliers:suppliers-list')
    fields = "__all__"


class SuppliersDeleteView(DeleteView):
    model = Suppliers
    template_name = ""
    success_url = reverse_lazy('suppliers:suppliers-list')
