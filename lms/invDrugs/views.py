from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from invDrugs.models import InvDrugs


class InvDrugsListView(ListView):
    
    model = InvDrugs
    template_name = "invDrugs/invDrugs-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = InvDrugs.objects.filter(Q(code=query))
            return object_list
        else:
            object_list = InvDrugs.objects.all()
            return object_list


class InvDrugsCreateView(CreateView):
    model = InvDrugs
    template_name = "invDrugs/invDrugs-form.html"
    success_url = reverse_lazy('invDrugs:invDrugs-list')
    fields = "__all__"


class InvDrugsUpdateView(UpdateView):
    model = InvDrugs
    template_name = "invDrugs/invDrugs-form.html"
    success_url = reverse_lazy('invDrugs:invDrugs-list')
    fields = "__all__"


class InvDrugsDeleteView(DeleteView):
    model = InvDrugs
    template_name = ""
    success_url = reverse_lazy('invDrugs:invDrugs-list')

def request(iid):
    object_list = InvEquipments.objects.filter(Q(id=iid))
    return object_list