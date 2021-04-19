from django.urls import path
from thyrod.views import ThyrodListView, ThyrodCreateView, ThyrodUpdateView, ThyrodDeleteView

app_name = 'thyrod'
urlpatterns = [
    path('', ThyrodListView.as_view(), name='thyrod-list'),
    path('create', ThyrodCreateView.as_view(), name='thyrod-create'),
    path('update/<int:pk>', ThyrodUpdateView.as_view(), name='thyrod-update'),
    path('delete/<int:pk>', ThyrodDeleteView.as_view(), name='thyrod-delete'),
    path('search', ThyrodListView.as_view(), name='thyrod-search')
]