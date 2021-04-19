from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView

# Create your views here.
from pmms.inventory.models import Inventory


class InventoryCreateView(CreateView):
    model = Inventory
    template_name = "inventory/inventory-form.html"
    success_url = reverse_lazy('inventory:inventory-list')
    fields = "__all__"

class InventoryUpdateView(UpdateView):
    model = Inventory
    template_name = "inventory/inventory-form.html"
    success_url = reverse_lazy('inventory:inventory-list')
    fields = "__all__"

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = ""
    success_url = ('inventory:inventory-list')

class InventoryListView(ListView):
    model = Inventory
    template_name = "inventory/inventory-form.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Inventory.objects.filter(Q(id =query))
            if object_list:
                return object_list
            else:
                return object_list
        else:
            object_list = Inventory.object.all()
            return object_list