
from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet, MedicalNoteViewSet


router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctoravailabilities', DoctorAvailabilityViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = router.urls