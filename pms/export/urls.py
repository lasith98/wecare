from django.urls import path

from export.views import ExportClinicalBook, dddd, generate_view

app_name = 'export'
urlpatterns = [
    path('clinical/book/<int:pk>', ExportClinicalBook.as_view(), name='export-clinical-book'),
    path('pdf/<int:id>/<str:view>', generate_view, name='pdf')

]
