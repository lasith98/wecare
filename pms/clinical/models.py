from django.db import models

from model_utils.models import TimeStampedModel

from choices.DurationTextChoice import DurationTextChoice
from choices.LabReportStatusChoice import LabReportStatusChoice
from choices.TimeChoice import TimeChoice
from patient.models import Patient


class ClinicalBook(TimeStampedModel):
    name = models.CharField(max_length=250)
    patient = models.ForeignKey(Patient, models.CASCADE)

    @property
    def records(self):
        return self.clinicalrecord_set.filter(clinical_book=self).all()


class ClinicalRecord(TimeStampedModel):
    diagnosis = models.TextField()
    clinical_book = models.ForeignKey(ClinicalBook, on_delete=models.CASCADE)

    @property
    def labs(self):
        return self.labreport_set.filter(clinical_record=self).all()

    @property
    def prescriptions(self):
        return self.prescription_set.filter(clinical_record=self).all()


class LabReport(models.Model):
    name = models.CharField(max_length=250)
    lab_report_id = models.CharField(max_length=250, default=-1)
    clinical_record = models.ForeignKey(ClinicalRecord, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=LabReportStatusChoice.choices,
                              default=LabReportStatusChoice.READY_TO_SEND_LAB)


class Prescription(models.Model):
    doug_id = models.IntegerField()
    doug_name = models.CharField(max_length=250)
    dose = models.IntegerField()
    time = models.CharField(max_length=30, choices=TimeChoice.choices, default=TimeChoice.MORNING)
    duration = models.IntegerField()
    duration_text = models.CharField(max_length=25, choices=DurationTextChoice.choices, default=DurationTextChoice.DAY)
    clinical_record = models.ForeignKey(ClinicalRecord, on_delete=models.CASCADE)
