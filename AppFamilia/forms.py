from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FamiliarFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    nacimiento= forms.DateField()

class EquipoFormulario(forms.Form):
    nombre= forms.CharField()
    pais= forms.CharField()
    imagen1= forms.ImageField()

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
    