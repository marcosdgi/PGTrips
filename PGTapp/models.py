from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.
class Cliente (models.Model):
    id = models.AutoField(primary_key= True)
    provincia = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero_casa = models.IntegerField()

class Acompañante (models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Reservacion(models.Model):
    codigo = models.AutoField(primary_key=True)
    Origen = models.CharField(max_length=50)
    Destino = models.CharField(max_length=50)
    Hora = models.TimeField(default=timezone.now)
    Fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s, %s, %s, %s' %(self.Origen, self.Destino, self.Hora, self.Fecha )

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    km_recorridos = models.IntegerField()
    #los campos de tipo imagen se configuran de esta manera para que cree una carpeta llamada autos 
    #donde se guardan las imagenes que vienen de la bdd
    imagen = models.ImageField(null=True, upload_to= 'autos')
class Chofer (models.Model):
    id = models.AutoField (primary_key=True)
    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Salario = models.IntegerField()


class Viaje (models.Model):
    id_Viaje = models.AutoField(primary_key=True)
    id_chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    id_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

class Destino(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.IntegerField()

class Viaje_Destino(models.Model):
    id_viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    id_destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
#este codigo fue comentado porque se utilizo el model user que ofrece django por defecto 
""" class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    email = models.EmailField()
    codigo = models.IntegerField()

    def __str__(self):
        return '%s, %s, %s, %s'%(self.nombre_usuario, self.contraseña, self.email, self.codigo) """
