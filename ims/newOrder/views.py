from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from newOrder.models import NewOrder


class NewOrderListView(ListView):
    model = NewOrder
    template_name = "newOrder/newOrder-list.html"
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = NewOrder.objects.filter(Q(code =query))
            return object_list
        else:
            object_list = NewOrder.objects.all()
            return object_list

class NewOrderCreateView(CreateView):
    model = NewOrder
    template_name = "newOrder/newOrder-form.html"
    success_url = reverse_lazy('newOrder:newOrder-list')
    fields = "__all__"


class NewOrderUpdateView(UpdateView):
    model = NewOrder
    template_name = "newOrder/newOrder-form.html"
    success_url = reverse_lazy('newOrder:newOrder-list')
    fields = "__all__"


class NewOrderDeleteView(DeleteView):
    model = NewOrder
    template_name = ""
    success_url = reverse_lazy('newOrder:newOrder-list')