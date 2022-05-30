from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppFamilia.models import Equipo

class FamiliarFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    nacimiento= forms.DateField()

class EquipoFormulario(forms.ModelForm):
    class Meta:
        model= Equipo
        fields=["nombre1", "pais", "imagen1"]

class MusicoFormulario(forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()

class RegistroFormulario(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)

class Meta:
    model= User
    fields=["username", "email", "password1", "password2"]
    