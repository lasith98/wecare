from django.urls import path

from clinical.views import ClinicalBookCreateView, ClinicalBookDeleteView, ClinicalBookUpdateView, ClinicalBookListView, \
    ClinicalBookDetailView, ClinicalRecordCreateView, ClinicalRecordUpdateView, lab_report_create, lab_report_delete, \
    prescription_create, send_data, prescription_delete

app_name = 'clinical'
urlpatterns = [
    path('doctor/book/list', ClinicalBookListView.as_view(), name='doctor-list'),
    path('doctor/book/create', ClinicalBookCreateView.as_view(), name='doctor-create'),
    path('doctor/book/update/<int:pk>', ClinicalBookUpdateView.as_view(), name='doctor-update'),
    path('doctor/book/delete/<int:pk>', ClinicalBookDeleteView.as_view(), name='doctor-delete'),
    path('doctor/book/detail/<int:pk>', ClinicalBookDetailView.as_view(), name='doctor-detail'),

    path('doctor/record/create/<int:id>', ClinicalRecordCreateView.as_view(), name='doctor-record'),
    path('doctor/record/update/<int:pk>', ClinicalRecordUpdateView.as_view(), name='doctor-record-update'),

    path('doctor/lab/report/create', lab_report_create, name='doctor-lab-report-create'),
    path('doctor/lab/report/delete/<int:id>', lab_report_delete, name='doctor-lab-report-delete'),

    path('doctor/prescription/create', prescription_create, name='doctor-prescription-create'),
    path('doctor/prescription/delete/<int:id>', prescription_delete, name='doctor-prescription-delete'),

    path('doctor/send', send_data, name='doctor-send-data'),
]
