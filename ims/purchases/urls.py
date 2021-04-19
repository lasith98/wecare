from django.urls import path
from purchases.views import PurchasesListView, PurchasesCreateView, PurchasesUpdateView, PurchasesDeleteView

app_name = 'purchases'
urlpatterns = [
    path('', PurchasesListView.as_view(), name='purchases-list'),
    path('create', PurchasesCreateView.as_view(), name='purchases-create'),
    path('update/<int:pk>', PurchasesUpdateView.as_view(), name='purchases-update'),
    path('delete/<int:pk>', PurchasesDeleteView.as_view(), name='purchases-delete'),
]