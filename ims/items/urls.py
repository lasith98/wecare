from django.urls import path
from items.views import ItemsListView, ItemsCreateView, ItemsUpdateView, ItemsDeleteView

app_name = 'items'
urlpatterns = [
    path('', ItemsListView.as_view(), name='items-list'),
    path('create', ItemsCreateView.as_view(), name='items-create'),
    path('update/<int:pk>', ItemsUpdateView.as_view(), name='items-update'),
    path('delete/<int:pk>', ItemsDeleteView.as_view(), name='items-delete'),
    path('search', ItemsListView.as_view(), name='items-search')
]