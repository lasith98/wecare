from django.urls import path
from newOrder.views import NewOrderListView, NewOrderCreateView, NewOrderUpdateView, NewOrderDeleteView

app_name = 'newOrder'
urlpatterns = [
    path('', NewOrderListView.as_view(), name='newOrder-list'),
    path('create', NewOrderCreateView.as_view(), name='newOrder-create'),
    path('update/<int:pk>', NewOrderUpdateView.as_view(), name='newOrder-update'),
    path('delete/<int:pk>', NewOrderDeleteView.as_view(), name='newOrder-delete'),
    path('search', NewOrderListView.as_view(), name='newOrder-search')
]