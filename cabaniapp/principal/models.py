from django.db import models
from perfil.models import PerfilCliente
from django.core.exceptions import ValidationError


class ComplejoCabanias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: {self.id} - {self.nombre}"
    
class Cabania(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    servicios = models.ManyToManyField('Servicio')
    idComplejo = models.ForeignKey(ComplejoCabanias,  to_field='id', on_delete=models.CASCADE)
    cantDormitorios = models.PositiveIntegerField()
    cantPersonas = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
     

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    id_complejo = models.ForeignKey(ComplejoCabanias, on_delete=models.CASCADE)
    id_cabania = models.ForeignKey(Cabania, on_delete=models.CASCADE)
    cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE)  # Relación uno a muchos con Cliente
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()


    def __str__(self):
        return f"Alquiler de {self.id_cabania} en {self.id_complejo} por {self.cliente}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre