from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from invEquipments.models import InvEquipments


class InvEquipmentsListView(ListView):
    model = InvEquipments
    template_name = "invEquipments/invEquipments-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = InvEquipments.objects.filter(Q(code=query))
            return object_list
        else:
            object_list = InvEquipments.objects.all()
            return object_list


class InvEquipmentsCreateView(CreateView):
    model = InvEquipments
    template_name = "invEquipments/invEquipments-form.html"
    success_url = reverse_lazy('invEquipments:invEquipments-list')
    fields = "__all__"


class InvEquipmentsUpdateView(UpdateView):
    model = InvEquipments
    template_name = "invEquipments/invEquipments-form.html"
    success_url = reverse_lazy('invEquipments:invEquipments-list')
    fields = "__all__"


class InvEquipmentsDeleteView(DeleteView):
    model = InvEquipments
    template_name = ""
    success_url = reverse_lazy('invEquipments:invEquipments-list')

def request(iid):
    object_list = InvEquipments.objects.filter(Q(id=iid))
    return object_list
