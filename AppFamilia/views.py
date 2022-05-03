from django.shortcuts import render
from AppFamilia.models import Equipo, Familiar, Musico
from django.http import HttpResponse
from AppFamilia.forms import FamiliarFormulario, EquipoFormulario, MusicoFormulario

def familiar(request):
    return render(request, "AppFamilia/familiar1.html")
   
def equipo(request):
    return render(request, "AppFamilia/equipo.html")

def musico(request):
    return render(request, "AppFamilia/musico.html")

def inicio(request):
    return render(request, "AppFamilia/inicio.html")

def familiarFormulario(request):
    if request.method == "POST":
        miFormulario= FamiliarFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            familiar= Familiar(nombre= informacion["nombre"], edad= informacion["edad"], nacimiento= informacion["nacimiento"])
            familiar.save()
            return render(request, "AppFamilia/inicio.html")
    else:
        miFormulario= FamiliarFormulario()
    return render (request, "AppFamilia/familiarFormulario.html", {"miFormulario": miFormulario})

def equipoFormulario(request):
    if request.method == "POST":
        miFormulario1= EquipoFormulario(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid():
            informacion= miFormulario1.cleaned_data
            equipo= Equipo(nombre1= informacion["nombre"], pais= informacion["pais"])
            equipo.save()
            return render(request, "AppFamilia/inicio.html")
    else:
        miFormulario1= EquipoFormulario()
    return render (request, "AppFamilia/equipoFormulario.html", {"miFormulario1": miFormulario1})

def musicoFormulario(request):
    if request.method == "POST":
        miFormulario2= MusicoFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid():
            informacion= miFormulario2.cleaned_data
            musico= Musico(nombre2= informacion["nombre"], genero= informacion["genero"])
            musico.save()
            return render(request, "AppFamilia/inicio.html")
    else:
        miFormulario2= MusicoFormulario()
    return render (request, "AppFamilia/musicoFormulario.html", {"miFormulario2": miFormulario2})


def busquedaFamiliar(request):
    return render (request, "AppFamilia/busquedaFamiliar.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        familiares= Familiar.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFamilia/resultadosBusqueda.html", {"familiares":familiares, "nombre":nombre})
    else:
        respuesta="No enviaste ningun dato"
    return HttpResponse(respuesta)

    

    



    



