from django.shortcuts import render
from AppFamilia.models import Avatar, Equipo, Familiar, Musico
from django.http import HttpResponse
from AppFamilia.forms import FamiliarFormulario, EquipoFormulario, MusicoFormulario, RegistroFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView   
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def about(request):
    return render(request, "AppFamilia/about.html")


def editarUsuario(request):
    usuario= request.user
    if request.method == "POST":
        miFormulario= RegistroFormulario(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.username= informacion["username"]
            usuario.email= informacion["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]
            usuario.save()
            return render(request, "AppFamilia/inicio.html")
    else:
        miFormulario= RegistroFormulario(initial={"username":usuario.username, "email":usuario.email})
    return render(request, "AppFamilia/editarUsuario.html", {"miFormulario":miFormulario, "usuario": usuario.username})



def register(request):
    if request.method == "POST":
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "AppFamilia/inicio.html", {"mensaje":"Usuario creado"})
    else:
        form = RegistroFormulario()
    return render(request, "AppFamilia/Registro.html", {"form":form})



def login_request(request):
    if request.method =="POST":
        form= AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user= authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return render(request, "AppFamilia/inicio.html", {"mensaje":f"Bienvenido {user}"})
        
        else:
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Error. Datos incorrectos"})
    else:
        form= AuthenticationForm()
    
    return render(request, "AppFamilia/login.html", {"form":form})


@login_required
def familiar(request):
    return render(request, "AppFamilia/familiar1.html")

@login_required  
def equipo(request):
    return render(request, "AppFamilia/equipo.html")

@login_required
def musico(request):
    return render(request, "AppFamilia/musico.html")

@login_required
def inicio(request):
    #avatares= Avatar.objects.filter(user=request.user.id)
    #imagen= avatares[0].imagen.url
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
        miFormulario1= EquipoFormulario(request.POST, request.FILES)
        print(miFormulario1)
        if miFormulario1.is_valid():
            informacion= miFormulario1.cleaned_data
            equipo= Equipo(nombre1= informacion["nombre1"], pais= informacion["pais"], imagen1= informacion["imagen1"])
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

def busquedaEquipo(request):
    return render (request, "AppFamilia/busquedaEquipo.html")

def busquedaMusico(request):
    return render (request, "AppFamilia/busquedaMusico.html")


def buscar(request): #familiar
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        familiares= Familiar.objects.filter(nombre__icontains=nombre)
        return render(request, "AppFamilia/resultadosBusqueda.html", {"familiares":familiares, "nombre":nombre})
    else:
        respuesta="No enviaste ningun dato"
    return HttpResponse(respuesta)

def buscar1(request): #familiar
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        equipos= Equipo.objects.filter(nombre1__icontains=nombre)
        return render(request, "AppFamilia/resultadosBusqueda1.html", {"equipos":equipos, "nombre":nombre})
    else:
        respuesta="No enviaste ningun dato"
    return HttpResponse(respuesta)

def buscar2(request): #familiar
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        musicos= Musico.objects.filter(nombre2__icontains=nombre)
        return render(request, "AppFamilia/resultadosBusqueda2.html", {"musicos":musicos, "nombre":nombre})
    else:
        respuesta="No enviaste ningun dato"
    return HttpResponse(respuesta)


def listaFamiliares(request):
    familiares = Familiar.objects.all()
    contexto = {"familiares":familiares}
    return render(request, "AppFamilia/leerFamiliares.html", contexto)


def borrarFamiliares(request, familiar_nombre):
    familiar= Familiar.objects.get(nombre=familiar_nombre)
    familiar.delete()
    familiares= Familiar.objects.all()
    contexto = {"familiares":familiares}
    return render(request, "AppFamilia/leerFamiliares.html", contexto)


def editarFamiliares(request, familiar_nombre):
    familiar= Familiar.objects.get(nombre=familiar_nombre)

    if request.method == "POST":
        miFormulario= FamiliarFormulario(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            familiar.nombre= informacion["nombre"]
            familiar.edad= informacion ["edad"]
            familiar.nacimiento= informacion ["nacimiento"]

            familiar.save()

            return render(request, "AppFamilia/inicio.html")
    else:
        miFormulario= FamiliarFormulario(initial={"nombre":familiar.nombre, "edad":familiar.edad, "nacimiento":familiar.nacimiento})
    return render(request, "AppFamilia/editarFamiliar.html",{'miFormulario':miFormulario, 'familiar_nombre':familiar_nombre})

class EquipoList(ListView):
    model= Equipo
    template_name= "AppFamilia/listaEquipos.html"

class EquipoDetalle(DetailView):
    model= Equipo
    template_name= "AppFamilia/equipoDetalle.html"

class EquipoCreacion(CreateView):
    model= Equipo
    success_url= "/AppFamilia/equipo/lista"
    fields= ["nombre1", "pais", "imagen1"]

class EquipoUpdate(UpdateView):
    model= Equipo
    success_url= "/AppFamilia/equipo/lista"
    fields= ["nombre1", "pais", "imagen1"]

class EquipoDelete(DeleteView):
    model= Equipo
    success_url= "/AppFamilia/equipo/lista"

#MUSICO

class MusicoList(ListView):
    model= Musico
    template_name= "AppFamilia/listaMusicos.html"

class MusicoDetalle(DetailView):
    model= Musico
    template_name= "AppFamilia/musicoDetalle.html"

class MusicoCreacion(CreateView):
    model= Musico
    success_url= "/AppFamilia/musico/lista"
    fields= ["nombre2", "genero"]

class MusicoUpdate(UpdateView):
    model= Musico
    success_url= "/AppFamilia/musico/lista"
    fields= ["nombre2", "genero"]

class MusicoDelete(DeleteView):
    model= Musico
    success_url= "/AppFamilia/musico/lista"

    

    

    

    



    



