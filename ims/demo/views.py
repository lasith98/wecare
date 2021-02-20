from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
from demo.models import Demo


class DemoListView(ListView):
    model = Demo
    template_name = "demo/demo-list.html"


class DemoCreateView(CreateView):
    model = Demo
    template_name = "demo/demo-form.html"
    success_url = reverse_lazy('demo:demo-list')
    fields = "__all__"


class DemoUpdateView(UpdateView):
    model = Demo
    template_name = "demo/demo-form.html"
    success_url = reverse_lazy('demo:demo-list')
    fields = "__all__"


class DemoDeleteView(DeleteView):
    model = Demo
    template_name = ""
    success_url = reverse_lazy('demo:demo-list')
