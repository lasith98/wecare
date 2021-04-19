from django.urls import path


from .views import attendanceList, attendanceCreateView,attendanceOutCreateView

app_name = 'mark_attendance_manual'

urlpatterns = [
    path('', attendanceList.as_view(), name='ams_admin_attendance_List'),
    path('create', attendanceCreateView.as_view(), name='ams_admin_attendance_create'),
    path('update/<int:pk>', attendanceOutCreateView.as_view(), name='ams_admin_attendance_create_out'),

]
