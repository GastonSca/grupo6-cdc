from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(max_length=10)
    telefono = models.CharField(max_length=150)
