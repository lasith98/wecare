from django.urls import path

from .views import ReportsListView, ReportsDeleteView



app_name = 'reports'




urlpatterns = [
    path('', ReportsListView.as_view(), name='reports-list'),

    path('delete/<int:pk>', ReportsDeleteView.as_view(), name='reports-delete'),
]
