from unittest.util import _MAX_LENGTH
from django.db import models

class Familiar(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    nacimiento= models.DateField()

class Equipo(models.Model):
    nombre1= models.CharField(max_length=40)
    pais= models.CharField(max_length=40)

class Musico(models.Model):
    nombre2= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)


