from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from medicine.models import Medicine


class MedicineListView(ListView):
    model = Medicine
    template_name = "medicine/medicine-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Medicine.objects.filter(Q(id =query))
            if object_list:
                return object_list
            else:
                return object_list
        else:
            object_list = Medicine.objects.all()
            return object_list

class MedicineCreateView(CreateView):
    model = Medicine
    template_name = "medicine/medicine-form.html"
    success_url = reverse_lazy('medicine:medicine-list')
    fields = "__all__"


class MedicineUpdateView(UpdateView):
    model = Medicine
    template_name = "medicine/medicine-form.html"
    success_url = reverse_lazy('medicine:medicine-list')
    fields = "__all__"


class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = ""
    success_url = reverse_lazy('medicine:medicine-list')