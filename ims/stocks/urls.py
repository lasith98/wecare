from django.urls import path
from stocks.views import StocksListView

app_name = 'stocks'
urlpatterns = [
    path('', StocksListView.as_view(), name='stocks-list')
]