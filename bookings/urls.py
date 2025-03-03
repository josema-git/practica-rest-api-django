from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('medicalnotes', MedicalNoteViewSet)