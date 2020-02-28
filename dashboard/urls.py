from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('analytic/', views.analytic_dashbaord, name='analyticDashboard'),
    path('client/', views.client_dashboard, name='clientDashboard'),
    path('nurse/', views.nurse_dashboard, name='nurseDashboard')
    # path('dashboard/patients/', views.patientsDashboard, name='patients_dashboard'),
    # path('dashboard/analytics/', views.analyticsDasboard, name='analytics_dashboard'),
]
