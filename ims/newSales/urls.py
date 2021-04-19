from django.urls import path
from newSales.views import NewSalesListView, NewSalesCreateView, NewSalesUpdateView, NewSalesDeleteView

app_name = 'newSales'
urlpatterns = [
    path('', NewSalesListView.as_view(), name='newSales-list'),
    path('create', NewSalesCreateView.as_view(), name='newSales-create'),
    path('update/<int:pk>', NewSalesUpdateView.as_view(), name='newSales-update'),
    path('delete/<int:pk>', NewSalesDeleteView.as_view(), name='newSales-delete'),
    path('search', NewSalesListView.as_view(), name='newSales-search')
]