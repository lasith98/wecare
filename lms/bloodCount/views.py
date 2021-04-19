from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from bloodCount.models import BloodCount


class BloodCountListView(ListView):
    model = BloodCount
    template_name = "bloodCount/bloodCount-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = BloodCount.objects.filter(Q(id=query))
            return object_list
        else:
            object_list = BloodCount.objects.all()
            return object_list


class BloodCountCreateView(CreateView):
    model = BloodCount
    template_name = "bloodCount/bloodCount-form.html"
    success_url = reverse_lazy('bloodCount:bloodCount-list')
    fields = "__all__"


class BloodCountUpdateView(UpdateView):
    model = BloodCount
    template_name = "bloodCount/bloodCount-form.html"
    success_url = reverse_lazy('bloodCount:bloodCount-list')
    fields = "__all__"


class BloodCountDeleteView(DeleteView):
    model = BloodCount
    template_name = ""
    success_url = reverse_lazy('bloodCount:bloodCount-list')
