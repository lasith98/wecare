from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from items.models import Items


class ItemsListView(ListView):
    model = Items
    template_name = "items/items-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Items.objects.filter(Q(code =query))
            return object_list
        else:
            object_list = Items.objects.all()
            return object_list

class ItemsCreateView(CreateView):
    model = Items
    template_name = "items/items-form.html"
    success_url = reverse_lazy('items:items-list')
    fields = "__all__"

class ItemsUpdateView(UpdateView):
    model = Items
    template_name = "items/items-form.html"
    success_url = reverse_lazy('items:items-list')
    fields = "__all__"


class ItemsDeleteView(DeleteView):
    model = Items
    template_name = ""
    success_url = reverse_lazy('items:items-list')
