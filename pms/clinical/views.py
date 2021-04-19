from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

# Create your views here.
from we_care_common.rabbitmq.SendMessage import SendMessage
from we_care_common.rabbitmq.constant.TopicConstant import PRESCRIPTION, LAB_REPORT

from apis.DrugApi import DrugApi
from apis.LabReportApi import LabReportApi
from choices.LabReportStatusChoice import LabReportStatusChoice
from clinical.models import ClinicalBook, ClinicalRecord, LabReport, Prescription
from clinical.serializers import LabReportSerializer, PrescriptionSerializer
from patient.serializers import PatientSerializer


class ClinicalBookListView(ListView):
    model = ClinicalBook
    template_name = "doctor/clinical-book-list.html"

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            return super().get_queryset().filter(patient_id=int(query))
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['delete_url'] = reverse_lazy('clinical:doctor-delete', kwargs={'pk': 1})
        return data


class ClinicalBookCreateView(CreateView):
    model = ClinicalBook
    template_name = 'doctor/clinical-book-form.html'
    success_url = reverse_lazy('clinical:doctor-list')
    fields = "__all__"


class ClinicalBookUpdateView(UpdateView):
    model = ClinicalBook
    template_name = 'doctor/clinical-book-form.html'
    success_url = reverse_lazy('clinical:doctor-list')
    fields = ["name"]


class ClinicalBookDeleteView(DeleteView):
    model = ClinicalBook
    template_name = ""
    success_url = reverse_lazy('clinical:doctor-list')


class ClinicalBookDetailView(DetailView):
    model = ClinicalBook
    template_name = 'doctor/clinical-book-detail.html'


class ClinicalRecordCreateView(CreateView):
    model = ClinicalRecord
    template_name = "doctor/clinical-record-form.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(self.kwargs['id'])
        data['book_id'] = self.kwargs['id']
        data['patient'] = ClinicalBook.objects.get(id=self.kwargs['id']).patient
        data['date'] = datetime.now()
        print(data)
        return data

    def get_success_url(self):
        return reverse('clinical:doctor-record-update', args=[self.object.id])


class ClinicalRecordUpdateView(UpdateView):
    model = ClinicalRecord
    template_name = "doctor/clinical-record-form.html"

    fields = ["diagnosis"]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        data['record_id'] = self.kwargs['pk']
        data['book_id'] = data['object'].clinical_book.id
        data["lab_report"] = LabReportApi().find_all()
        data["drugs"] = DrugApi().find_all()
        data['patient'] = data['object'].clinical_book.patient

        return data

    def get_success_url(self):
        return reverse('clinical:doctor-record-update', args=[self.kwargs['pk']])


def lab_report_create(request):
    if request.method == "POST":
        model = LabReportApi().find_by_id(int(request.POST.get('lab_report_id', 1)))
        record_id = int(request.POST.get('record_id'))
        LabReport.objects.update_or_create(name=model.name, lab_report_id=model.id, clinical_record_id=record_id)
        return redirect('clinical:doctor-record-update', pk=record_id)
    return HttpResponseNotFound('<h1>Page not found</h1>')


def lab_report_delete(request, id):
    if request.method == "POST":
        model = LabReport.objects.get(id=id)
        record_id = model.clinical_record.id
        model.delete()
        return redirect('clinical:doctor-record-update', pk=record_id)
    return HttpResponseNotFound('<h1>Page not found</h1>')


def prescription_create(request):
    if request.method == "POST":
        model = DrugApi().find_by_id(int(request.POST.get('drug_id', 1)))
        record_id = int(request.POST.get('record_id'))
        print(request.POST)
        Prescription.objects.update_or_create(doug_name=model.name,
                                              doug_id=model.id,
                                              clinical_record_id=record_id,
                                              dose=int(request.POST.get("dose", 0)),
                                              time=request.POST.get("time", 'N/A'),
                                              duration=int(request.POST.get("duration", 0)),
                                              duration_text=request.POST.get("duration_text", 'N/A')
                                              )
        return redirect('clinical:doctor-record-update', pk=record_id)
    return HttpResponseNotFound('<h1>Page not found</h1>')


def prescription_delete(request, id):
    if request.method == "POST":
        model = Prescription.objects.get(id=id)
        record_id = model.clinical_record.id
        model.delete()
        return redirect('clinical:doctor-record-update', pk=record_id)
    return HttpResponseNotFound('<h1>Page not found</h1>')


def send_data(request):
    if request.method == "POST":
        try:
            record = ClinicalRecord.objects.get(id=int(request.POST.get('record_id')))
            if record.labs:
                for model in record.labs:
                    model.status = LabReportStatusChoice.IN_QUEUE
                    model.save()
                SendMessage(LAB_REPORT).send(
                    {"patient": PatientSerializer(record.clinical_book.patient).data,
                     'report': LabReportSerializer(record.labs, many=True).data},
                    '')
            if record.prescriptions:
                SendMessage(PRESCRIPTION).send({"patient": PatientSerializer(record.clinical_book.patient).data,
                                                'prescription': PrescriptionSerializer(record.prescriptions,
                                                                                       many=True).data},
                                               '')

            return redirect('clinical:doctor-detail', pk=record.clinical_book.id)
        except ClinicalRecord.DoesNotExist:
            pass

    return HttpResponseNotFound('<h1>Page not found</h1>')
