from rest_framework.routers import DefaultRouter

from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('insurances', InsuranceViewSet)
router.register('medicalrecords', MedicalRecordViewSet)

urlpatterns = router.urls
