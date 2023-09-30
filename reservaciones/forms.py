from django import forms
from PGTapp.models import Reservacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class reservacion(forms.ModelForm):
    """ Aqui la clase meta hereda los campos del modelo llamado Reservacion """
    class Meta():
        model = Reservacion
        fields = [
            'codigo', 'Origen', 'Destino', 'Fecha', 'Hora'
        ]   
        widgets = {
            'destino': forms.TextInput(attrs={'class':'inputR'}),
            'origen' : forms.TextInput(attrs={'class':'inputR'}),
            'Fecha' : forms.DateInput(attrs={'class':'inputdate'}),
            'Hora' : forms.TimeInput(attrs={'class':'inputtime'})
        }
        
#Este formulario sera utilizado para guardar los usuarios que se registren dentro de la aplicacion debera ser modificado en el futuro para organizarlo mejor
class Usuario(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = [
            'username','email'
        ]
        widgets = {
            'username':forms.TextInput(attrs={'class':'inputU'}),
            'password':forms.PasswordInput(attrs={'class':'inputU'}),
            'Confirm password':forms.PasswordInput(attrs={'class':'inputU'}),
            'email':forms.EmailInput(attrs={'class':'inputU'})
        }
