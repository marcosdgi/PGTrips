from django.shortcuts import render

# Create your views here.
def base (request):
    return render (request, "Base.html")


def homepage (request):
    return render(request, "Homepage.html")

def reservaciones (request):
    return render (request,"Reservaciones.html")

def transportes (request):
    return render (request, "Transportes.html")
def programacion (request):
    return render (request, "Programacion.html")