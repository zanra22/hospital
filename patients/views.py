from django.shortcuts import render
from .models import *

def patientsList(request):

    patient = Patient.objects.all()
    context = {
        'patient' : patient
    }

    return render(request, 'patients/views/patients_table.html', context)
