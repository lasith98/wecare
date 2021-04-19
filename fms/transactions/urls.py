from django.urls import path

from .views import TransactionsReadView, TransactionsCreateView, TransactionsUpdateView,\
    TransactionsDeleteView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionsReadView.as_view(), name='transactions-list'),
    path('create', TransactionsCreateView.as_view(), name='transactions-create'),
    path('update/<int:pk>', TransactionsUpdateView.as_view(), name='transactions-update'),
    path('delete/<int:pk>', TransactionsDeleteView.as_view(), name='transactions-delete'),
]
