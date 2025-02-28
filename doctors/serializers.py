from rest_framework import serializers
from .models import Doctor, Department, Doctor_Availability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class Doctor_AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Availability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'