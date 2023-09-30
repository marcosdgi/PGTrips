from django import forms
from PGTapp.models import Auto

class AutoForm(forms.ModelForm):
    archivo = forms.FileField()
    class Meta():
        model = Auto
        fields = [
        'placa', 'modelo', 'km_recorridos', 'imagen', 'archivo'
    ]
        widgets = {
        'placa': forms.TextInput(attrs={'class':'input'}),
        'modelo':forms.TextInput(attrs={'class':'input'}),
        'km_recorridos':forms.NumberInput(attrs={'class':'input'}),
        'imagen':forms.HiddenInput(),
        'archivo':forms.FileInput(attrs={'class':'input'})
    }