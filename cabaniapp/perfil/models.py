from django.db import models



class Administrador(models.Model):
    ##usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos necesarios
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=100)
    dni = models.CharField(verbose_name="Dni",max_length=10)
    fecha_nacimiento = models.DateField(verbose_name="Nacimiento")
    telefono = models.CharField(verbose_name="Telefono",max_length=20)

