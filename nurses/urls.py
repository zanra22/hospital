from django.urls import path
from . import views

urlpatterns = [
    path('list/nurses/', views.nursesList, name='nurses_list'),
]
