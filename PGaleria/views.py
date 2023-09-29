from django.shortcuts import render
from PGTapp.models import Auto 
from django.contrib.auth.decorators import login_required

@login_required
def Galeria(request):
    autos = Auto.objects.all()
    return render(request, 'Galeria.html',{'autos':autos})
