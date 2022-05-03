from django.urls import path
from AppFamilia import views

urlpatterns = [
    path("familiares/", views.familiar, name="Familiares"),
    path("equipos/", views.equipo, name="Equipos"),
    path("musicos/", views.musico, name="Musicos"),
    path("", views.inicio, name="Inicio"),
    path("familiarFormulario/", views.familiarFormulario, name="familiarFormulario"),
    path("busquedaFamiliar/", views.busquedaFamiliar, name="BusquedaFamiliar"),
    path("buscar/", views.buscar),
    path("equipoFormulario/", views.equipoFormulario, name="equipoFromulario"),
    path("musicoFormulario/", views.musicoFormulario, name="musicoFormulario"),

]