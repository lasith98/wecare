from django.urls import path

from .views import AccountsListView, AccountsCreateView, AccountsUpdateView,\
    AccountsDeleteView
app_name = 'accounts'

urlpatterns = [
    path('', AccountsListView.as_view(), name='accounts-list'),
    path('create', AccountsCreateView.as_view(), name='accounts-create'),
    path('update/<int:pk>', AccountsUpdateView.as_view(), name='accounts-update'),
    path('delete/<int:pk>', AccountsDeleteView.as_view(), name='accounts-delete'),
]
