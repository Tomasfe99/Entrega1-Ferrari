from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

class Familiar(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre} - Edad:{self.edad} - nacimiento:{self.nacimiento}"

    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    nacimiento= models.DateField()

class Equipo(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre1} - Pais:{self.pais}"
    nombre1= models.CharField(max_length=40)
    pais= models.CharField(max_length=40)
    imagen1= models.ImageField(upload_to= "equipos", null=True, blank=True)

class Musico(models.Model):
    def __str__(self):
        return f"Nombre:{self.nombre2} - Genero:{self.genero}"
    nombre2= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    imagen= models.ImageField(upload_to= "avatares", null=True, blank=True)
    





