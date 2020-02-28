from django.shortcuts import render
from .models import Doctor

def doctorsList(request):

    doctor = Doctor.objects.all()

    context = {
        'doctor' : doctor
    }

    return render(request, 'doctors/views/doctors_table.html', context)
