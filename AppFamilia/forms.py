from django import forms
class FamiliarFormulario(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()
    nacimiento= forms.DateField()

class EquipoFormulario(forms.Form):
    nombre= forms.CharField()
    pais= forms.CharField()

class MusicoFormulario(forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()