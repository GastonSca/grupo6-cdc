from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(max_length=10)
    telefono = models.CharField(max_length=150)

    

    class Meta:
        abstract = True

class Perfil(Persona): #Relacion 1 a 1. Cada Perfil es una Persona
    nivelAutorizacion = models.IntegerField()
    def _str_(self):
        return f' {self.nombre} - {self.apellido}'
    
class PerfilCliente(Persona):
    antecedentes = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

