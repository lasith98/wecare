from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from newSales.models import NewSales


class NewSalesListView(ListView):
    model = NewSales
    template_name = "newSales/newSales-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = NewSales.objects.filter(Q(code =query))
            return object_list
        else:
            object_list = NewSales.objects.all()
            return object_list

class NewSalesCreateView(CreateView):
    model = NewSales
    template_name = "newSales/newSales-form.html"
    success_url = reverse_lazy('newSales:newSales-list')
    fields = "__all__"


class NewSalesUpdateView(UpdateView):
    model = NewSales
    template_name = "newSales/newSales-form.html"
    success_url = reverse_lazy('newSales:newSales-list')
    fields = "__all__"


class NewSalesDeleteView(DeleteView):
    model = NewSales
    template_name = ""
    success_url = reverse_lazy('newSales:newSales-list')
