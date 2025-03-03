from  rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer 

    @action(detail=True, methods=['POST'], url_path='set-on-vacation')
    def set_on_vacation(self, request, id):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({'is_on_vacation': doctor.is_on_vacation})
    
    @action(detail=True, methods=['POST'], url_path='set-off-vacation')
    def set_off_vacation(self, request, id):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'is_on_vacation': doctor.is_on_vacation})

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer