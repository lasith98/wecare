from django.urls import path
from bloodCount.views import BloodCountListView, BloodCountCreateView, BloodCountUpdateView, BloodCountDeleteView

app_name = 'bloodCount'
urlpatterns = [
    path('', BloodCountListView.as_view(), name='bloodCount-list'),
    path('create', BloodCountCreateView.as_view(), name='bloodCount-create'),
    path('update/<int:pk>', BloodCountUpdateView.as_view(), name='bloodCount-update'),
    path('delete/<int:pk>', BloodCountDeleteView.as_view(), name='bloodCount-delete'),
    path('search', BloodCountListView.as_view(), name='bloodCount-search')
]