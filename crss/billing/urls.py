from django.urls import path

from billing.views import BillingListView, BillingCreateView, BillingUpdateView, BillingDeleteView


app_name = 'billing'
urlpatterns = [
    path('', BillingListView.as_view(), name='billing-list'),
    path('create', BillingCreateView.as_view(), name='billing-create'),
    path('update/<int:pk>', BillingUpdateView.as_view(), name='billing-update'),
    path('delete/<int:pk>', BillingDeleteView.as_view(), name='billing-delete'),
]
