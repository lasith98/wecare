from django.urls import path

from .views import BalanceSheetListView, BalanceSheetUpdateView, BalanceSheetCreateView, BalanceSheetDeleteView

app_name = 'balanceSheet'



urlpatterns = [
    path('', BalanceSheetListView.as_view(), name='balanceSheet-list'),
    path('create', BalanceSheetCreateView.as_view(), name='balanceSheet-create'),
    path('update/<int:pk>', BalanceSheetUpdateView.as_view(), name='balanceSheet-update'),
    path('delete/<int:pk>', BalanceSheetDeleteView.as_view(), name='balanceSheet-delete'),
]
