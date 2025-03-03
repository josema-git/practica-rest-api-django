from rest_framework import generics 
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer

class AppointmentView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class MedicalNoteView(generics.ListCreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()