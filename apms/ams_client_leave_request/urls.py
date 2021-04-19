from django.urls import path


from .views import leaveListView, leaveCreateView, leaveUpdateView, leaveDeleteView

app_name = 'ams_client_leave_request'

urlpatterns = [
    path('', leaveListView.as_view(), name='ams_client_leave_request-List'),
    path('create', leaveCreateView.as_view(), name='ams_client_leave_request-create'),
    path('update/<int:pk>', leaveUpdateView.as_view(), name='ams_client_leave_request-update'),
    path('delete/<int:pk>', leaveDeleteView.as_view(), name='ams_client_leave_request-delete'),
]
