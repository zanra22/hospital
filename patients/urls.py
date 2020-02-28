from django.urls import path
from . import views

urlpatterns = [

    path('list/patients/', views.patientsList, name='patients_list'),
]
