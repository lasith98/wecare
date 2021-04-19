


from django.urls import reverse_lazy

# Create your views here.
from .models import Transaction
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView




class TransactionsReadView(ListView):
    model = Transaction
    template_name = "transactions/view-transactions-list.html"


class TransactionsCreateView(CreateView):
    model = Transaction
    template_name = "transactions/new-transactions-form.html"
    success_url = reverse_lazy('transactions:transactions-list')
    fields = ['transaction_id','date', 'account_no', 'description', 'total_amount']


class TransactionsUpdateView(UpdateView):
    model = Transaction
    template_name = "transactions/new-transactions-form.html"
    success_url = reverse_lazy('transactions:transactions-list')
    fields = "__all__"


class TransactionsDeleteView(DeleteView):
    model = Transaction
    template_name = ""
    success_url = reverse_lazy('transactions:transactions-list')


