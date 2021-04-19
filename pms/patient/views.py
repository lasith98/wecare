from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import CreateAPIView

# Create your views here.
from apis.BillingApi import BillingApi
from choices.LabReportStatusChoice import LabReportStatusChoice
from clinical.models import ClinicalBook
from patient.serializers import PatientSerializer

patient_id = 1


class PatientCreateAPIView(CreateAPIView):
    serializer_class = PatientSerializer


class PatientClinicalBook(ListView):
    model = ClinicalBook
    template_name = 'patient/patient-clinical-book.html'

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return super().get_queryset().filter(patient_id=patient_id, name__icontains=query)
        return super().get_queryset().filter(patient_id=patient_id)


class PatientClinicalBookDetailView(DetailView):
    model = ClinicalBook
    template_name = 'patient/patient-clinical-book-detail.html'


def wallet(request):
    return render(request, 'patient/wallet.html', context={'object_list': BillingApi().find_all()})


def care_me(request):
    return render(request, 'patient/care-me.html')


def dashboard(request):
    return render(request, 'patient/dashboard.html', context={
        'pending_lab_report': ClinicalBook.objects.filter(patient_id=patient_id,
                                                          clinicalrecord__labreport__status=LabReportStatusChoice.IN_QUEUE).count(),
        'clinical_books': ClinicalBook.objects.filter(patient_id=patient_id).count()

    })
