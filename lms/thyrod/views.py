from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from thyrod.models import Thyrod


class ThyrodListView(ListView):
    model = Thyrod
    template_name = "thyrod/thyrod-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Thyrod.objects.filter(Q(id=query))
            return object_list
        else:
            object_list = Thyrod.objects.all()
            return object_list


class ThyrodCreateView(CreateView):
    model = Thyrod
    template_name = "thyrod/thyrod-form.html"
    success_url = reverse_lazy('thyrod:thyrod-list')
    fields = "__all__"


class ThyrodUpdateView(UpdateView):
    model = Thyrod
    template_name = "thyrod/thyrod-form.html"
    success_url = reverse_lazy('thyrod:thyrod-list')
    fields = "__all__"


class ThyrodDeleteView(DeleteView):
    model = Thyrod
    template_name = ""
    success_url = reverse_lazy('thyrod:thyrod-list')

