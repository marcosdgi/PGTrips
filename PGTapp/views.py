from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from reservaciones.forms import Usuario 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

@method_decorator(login_required, name = 'dispatch')
def inicio_sesion (request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['passworod']
       user = authenticate(request, username = username, password = password)
       if user is not None:
           login(request,user)
           return redirect('Homepage.html')
       else:
           error_message = 'Credenciales Invalidas, intentelo de nuevo.'
           return render (request, 'Login.html', {'error message': error_message})
       
   else:
       return render (request, 'Login.html')
       
class CustomLoginView(LoginView):
    template_name = 'Login.html'

@login_required
def base (request):
    return render (request, "Base.html")


@login_required
def homepage (request):
    return render(request, "Homepage.html")
@login_required
def reservaciones (request):
    return render (request,"Reservaciones.html")

@login_required
def transportes (request):
    return render (request, "Transportes.html")

@login_required
def programacion (request):
    return render (request, "Programacion.html")
@login_required
def informacion (request):

    return render (request, "Informacion.html")