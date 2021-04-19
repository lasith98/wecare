from django.urls import path

from patient.views import PatientCreateAPIView, PatientClinicalBook, PatientClinicalBookDetailView, wallet, care_me, \
    dashboard

app_name = 'patient'
urlpatterns = [
    path('api/create', PatientCreateAPIView.as_view(), name='api-create'),
    path('clinical/book', PatientClinicalBook.as_view(), name='clinical-book-list'),
    path('clinical/book/detail/<int:pk>', PatientClinicalBookDetailView.as_view(), name='clinical-book-detail'),
    path('wallet', wallet, name='wallet'),
    path('care/me', care_me, name='care_me'),
    path('dashboard', dashboard, name='dashboard'),

]
