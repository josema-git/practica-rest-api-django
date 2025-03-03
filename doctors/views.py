from rest_framework import generics
from .models import Doctor,  Department , DoctorAvailability, MedicalNote
from .serializers import DoctorSerializer, DepartmentSerializer , DoctorAvailabilitySerializer, MedicalNoteSerializer
 
# Create your views here. 

class list_doctorsView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class detail_doctorView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class list_departmentsView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class list_doctor_availabilitiesView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class detail_doctor_availabilityView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class list_medical_notesView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
