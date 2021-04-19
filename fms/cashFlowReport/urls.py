from django.urls import path

from .views import CashFlowListView, CashFlowCreateView, CashFlowUpdateView,\
    CashFlowDeleteView

app_name = 'cashFlowReport'



urlpatterns = [
    path('', CashFlowListView.as_view(), name='cashFlow-list'),
    path('create', CashFlowCreateView.as_view(), name='cashFlow-create'),
    path('update/<int:pk>', CashFlowUpdateView.as_view(), name='cashFlow-update'),
    path('delete/<int:pk>', CashFlowDeleteView.as_view(), name='cashFlow-delete'),
]
