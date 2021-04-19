from django.urls import path

from guest.views import GuestListView, GuestCreateView, GuestUpdateView, GuestDeleteView

app_name = 'guest'
urlpatterns = [
    path('', GuestListView.as_view(), name='guest-list'),
    path('create', GuestCreateView.as_view(), name='guest-create'),
    path('update/<int:pk>', GuestUpdateView.as_view(), name='guest-update'),
    path('delete/<int:pk>', GuestDeleteView.as_view(), name='guest-delete'),
]
