from django.shortcuts import render
from reservaciones.forms import reservacion,Usuario
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Reserva(request):
    if request.method == 'POST':
        formularioR = reservacion(request.POST)

        if formularioR.is_valid():
            formularioR.save()
            return render(request, 'Recibido.html')
    else:
        formularioR = reservacion()

    return render(request, 'reservacion.html', {'formularioR': formularioR })



def registro(request):
    if request.method == 'POST':
        FormularioRegistro = Usuario(request.POST)
        if FormularioRegistro.is_valid():
            FormularioRegistro.save()
            return render(request, 'Homepage.html')
        
    else:
        FormularioRegistro = Usuario()
    
    return render(request, 'Registro.html',{'formularioRegistro':FormularioRegistro})
