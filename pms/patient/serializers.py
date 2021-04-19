from rest_framework import serializers

from patient.models import Patient, Guardian


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    guardian = GuardianSerializer()

    class Meta:
        model = Patient
        fields = "__all__"

    def create(self, validated_data):
        g_data = validated_data.pop('guardian')
        guardian = Guardian.objects.create(**g_data)
        instance = Patient.objects.create(**validated_data, guardian=guardian)
        instance.save()
        return instance
