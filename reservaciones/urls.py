from django.urls import path
from reservaciones.views import *

urlpatterns = [
  path ('reservaciones/', Reserva, name='reservaciones'),
  path ('registro/',registro, name='registro'),
]