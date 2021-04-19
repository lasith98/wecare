from django.urls import path

app_name = 'mockup'
urlpatterns = [
    path('doctor/list', ClinicalBookListView.as_view(), name='doctor-list'),
]
