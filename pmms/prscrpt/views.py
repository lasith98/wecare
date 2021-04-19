from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from prscrpt.models import Prscrpt


class PrscrptListView(ListView):
    model = Prscrpt
    template_name = "prscrpt/prscrpt-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Prscrpt.objects.filter(Q(id =query))
            return object_list
        else:
            object_list = Prscrpt.objects.all()
            return object_list

class PrscrptCreateView(CreateView):
    model = Prscrpt
    template_name = "prscrpt/prscrpt-form.html"
    success_url = reverse_lazy('prscrpt:prscrpt-list')
    fields = "__all__"


class PrscrptUpdateView(UpdateView):
    model = Prscrpt
    template_name = "prscrpt/prscrpt-form.html"
    success_url = reverse_lazy('prscrpt:prscrpt-list')
    fields = "__all__"


class PrscrptDeleteView(DeleteView):
    model = Prscrpt
    template_name = ""
    success_url = reverse_lazy('prscrpt:prscrpt-list')