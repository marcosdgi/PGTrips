from django.shortcuts import render
from reservaciones.forms import reservacion
from reservaciones.forms import Usuario
# Create your views here.

def Reserva(request):
    if request.method == 'POST':
        formularioR = reservacion(request.POST)

        if formularioR.is_valid():
            formularioR.save()
            return render(request, 'Recibido.html')
    else:
        formularioR = reservacion()

    return render(request, 'reservacion.html', {'formularioR': formularioR })




def Registrar(request):
    if request.method == 'POST':
        Registro = Usuario(request.POST)

        if Registro.is_valid():
            Registro.save()
            return render(request, 'Base.html')
