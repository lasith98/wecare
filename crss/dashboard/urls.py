from django.urls import path

from dashboard.views import dashboard, test, patient_reg

app_name = 'dashboard'
urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('',test, name='test'),
    path('patient_reg',patient_reg, name='patient_reg'),

]
