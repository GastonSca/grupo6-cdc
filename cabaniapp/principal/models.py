from django.db import models

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
