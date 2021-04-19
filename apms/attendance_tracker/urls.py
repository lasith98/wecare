from django.urls import path



from .views import attendanceChartView

app_name = 'attendance_tracker'

urlpatterns = [
    path('', attendanceChartView.as_view(), name='allowance-List'),

]
