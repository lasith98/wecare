from django.urls import path
from suppliers.views import SuppliersListView, SuppliersCreateView, SuppliersUpdateView, SuppliersDeleteView

app_name = 'suppliers'
urlpatterns = [
    path('', SuppliersListView.as_view(), name='suppliers-list'),
    path('create', SuppliersCreateView.as_view(), name='suppliers-create'),
    path('update/<int:pk>', SuppliersUpdateView.as_view(), name='suppliers-update'),
    path('delete/<int:pk>', SuppliersDeleteView.as_view(), name='suppliers-delete'),
    path('search', SuppliersListView.as_view(), name='suppliers-search')
]