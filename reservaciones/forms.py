from django import forms
from PGTapp.models import Reservacion,Usuario

class reservacion(forms.ModelForm):
    """ dia = forms.DateField()
    horario = forms.DateTimeField()
    destino = forms.CharField(max_length=50) """
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
        
#Este formulario sera utilizado para guardar los usuarios que se registren dentro de la aplicacion
class Usuario(forms.ModelForm):
    class Meta():
        model = Usuario
        fields = [
            'codigo','nombre_usuario', 'contraseña','email'
        ]
        widgets = {
            'codigo':forms.NumberInput(attrs={'class':'inputU'}),
            'nombre_usuario':forms.TextInput(attrs={'class':'inputU'}),
            'contraseña':forms.PasswordInput(attrs={'class':'inputU'}),
            'email':forms.EmailInput(attrs={'class':'inputU'})
        }