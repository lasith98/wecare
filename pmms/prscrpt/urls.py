from django.urls import path
from prscrpt.views import PrscrptListView, PrscrptCreateView, PrscrptUpdateView, PrscrptDeleteView

app_name = 'prscrpt'
urlpatterns = [
    path('', PrscrptListView.as_view(), name='prscrpt-list'),
    path('create', PrscrptCreateView.as_view(), name='prscrpt-create'),
    path('update/<int:pk>', PrscrptUpdateView.as_view(), name='prscrpt-update'),
    path('delete/<int:pk>', PrscrptDeleteView.as_view(), name='prscrpt-delete'),
    path('search', PrscrptListView.as_view(), name='prscrpt-search')
]