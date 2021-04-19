from django.urls import path
from inventory.views import InventoryCreateView, InventoryUpdateView, InventoryDeleteView, InventoryListView

app_name = 'inventory'
urlpatterns = [
    path('create', InventoryCreateView.as_view(), name='inventory-create'),
    path('update/<int:pk>', InventoryUpdateView.as_view(), name='inventory-update'),
    path('delete/<int:pk>', InventoryDeleteView.as_view(), name='inventory-delete'),
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('search', InventoryListView.as_view(), name='inventory-search')
]