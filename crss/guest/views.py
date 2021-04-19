from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.

from guest.models import Guest


class GuestListView(ListView):
    model = Guest
    template_name = "guest/guest-list.html"


class GuestCreateView(CreateView):
    model = Guest
    template_name = "guest/guest-form.html"
    success_url = reverse_lazy('guest:guest-list')
    fields = "__all__"


class GuestUpdateView(UpdateView):
    model = Guest
    template_name = "guest/guest-form.html"
    success_url = reverse_lazy('guest:guest-list')
    fields = "__all__"


class GuestDeleteView(DeleteView):
    model = Guest
    template_name = ""
    success_url = reverse_lazy('guest:guest-list')

