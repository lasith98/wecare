from django.urls import path
from invDrugs.views import InvDrugsListView, InvDrugsCreateView, InvDrugsUpdateView, InvDrugsDeleteView , request

app_name = 'invDrugs'
urlpatterns = [
    path('', InvDrugsListView.as_view(), name='invDrugs-list'),
    path('create', InvDrugsCreateView.as_view(), name='invDrugs-create'),
    path('update/<int:pk>', InvDrugsUpdateView.as_view(), name='invDrugs-update'),
    path('delete/<int:pk>', InvDrugsDeleteView.as_view(), name='invDrugs-delete'),
    path('search', InvDrugsListView.as_view(), name='invDrugs-search'),
    path('request/<int:pk>', request, name='invDrugs-request')
]