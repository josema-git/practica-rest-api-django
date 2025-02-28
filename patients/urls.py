from django.urls import path, include

from .views import list_patients, detail_patient

urlpatterns = [
    path('patients', list_patients),
    path('patients/<int:id>/', detail_patient)
]
