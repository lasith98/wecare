


from django.urls import reverse_lazy

# Create your views here.
from .models import Account
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView




class AccountsListView(ListView):
    model = Account
    template_name = "accounts/accounts-list.html"


class AccountsCreateView(CreateView):
    model = Account
    template_name = "accounts/accounts-form.html"
    success_url = reverse_lazy('accounts:accounts-list')
    fields = "__all__"


class AccountsUpdateView(UpdateView):
    model = Account
    template_name = "accounts/accounts-form.html"
    success_url = reverse_lazy('accounts:accounts-list')
    fields = "__all__"


class AccountsDeleteView(DeleteView):
    model = Account
    template_name = ""
    success_url = reverse_lazy('accounts:accounts-list')


