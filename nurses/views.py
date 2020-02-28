from django.shortcuts import render
from .models import *

def nursesList(request):

    nurse = Nurse.objects.all()

    context = {
        'nurse' : nurse
    }

    return render(request, 'nurses/views/nurses_table.html', context)


