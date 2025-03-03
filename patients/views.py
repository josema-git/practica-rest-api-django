from rest_framework.decorators import api_view
from rest_framework import generics

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class list_patientsView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class detail_patientView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class list_insurancesView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class detail_insuranceView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()

class list_medical_recordsView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()