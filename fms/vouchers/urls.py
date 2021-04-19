from django.urls import path

from .views import VouchersListView, VouchersCreateView, VouchersUpdateView, VouchersDeleteView



app_name = 'vouchers'




urlpatterns = [
    path('', VouchersListView.as_view(), name='vouchers-list'),
    path('create', VouchersCreateView.as_view(), name='vouchers-create'),
    path('update/<int:pk>', VouchersUpdateView.as_view(), name='vouchers-update'),
    path('delete/<int:pk>', VouchersDeleteView.as_view(), name='vouchers-delete'),
]
