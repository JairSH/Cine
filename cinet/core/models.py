from django.db import models

# Create your models here.

class Genero(models.Model):
    #id -> numero autoincrementable
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField()
    anio = models.IntegerField(verbose_name='Año')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre