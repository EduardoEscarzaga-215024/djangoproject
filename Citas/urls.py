from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar_cita, name = 'agendar_cita')
]