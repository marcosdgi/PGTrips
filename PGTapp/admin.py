from django.contrib import admin
from PGTapp.models import *
# Registrando los modelos 
admin.site.register(Cliente)
admin.site.register(Acompañante)
admin.site.register(Auto)
admin.site.register(Reservacion)
admin.site.register(Viaje)
admin.site.register(Viaje_Destino)
admin.site.register(Chofer)
admin.site.register(Destino)
