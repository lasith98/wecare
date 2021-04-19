from rest_framework import serializers

from clinical.models import Prescription, LabReport


class LabReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
