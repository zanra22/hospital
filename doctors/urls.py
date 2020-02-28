from django.urls import path
from . import views


urlpatterns = [

    path('list/doctors/', views.doctorsList, name='doctors_list'),
]
