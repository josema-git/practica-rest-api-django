from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PatientSerializer
from .models import Patient


@api_view(['GET', 'POST'])
def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def detail_patient(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = PatientSerializer(patient, data = request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        