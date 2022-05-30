from django.urls import path
from AppFamilia import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("familiares/", views.familiar, name="Familiares"),
    path("equipos/", views.equipo, name="Equipos"),
    path("musicos/", views.musico, name="Musicos"),
    path("", views.inicio, name="Inicio"),
    path("familiarFormulario/", views.familiarFormulario, name="familiarFormulario"),
    path("busquedaFamiliar/", views.busquedaFamiliar, name="BusquedaFamiliar"),
    path("buscar/", views.buscar),
    path("equipoFormulario/", views.equipoFormulario, name="equipoFromulario"),
    path("busquedaEquipo/", views.busquedaEquipo, name="BusquedaEquipo"),
    path("buscar1/", views.buscar1),
    path("busquedaMusico/", views.busquedaMusico, name="BusquedaMusico"),
    path("buscar2/", views.buscar2), 
    path("musicoFormulario/", views.musicoFormulario, name="musicoFormulario"),
    path("listaFam/", views.listaFamiliares, name="listaFamiliares"),
    path("chauFamiliar/<familiar_nombre>/", views.borrarFamiliares, name="BorrarFamiliares"),
    path("editarFamiliar/<familiar_nombre>/", views.editarFamiliares, name="EditarFamiliares"),

    path("equipo/lista", views.EquipoList.as_view(), name= "ListEquipos"),
    path(r"^(?P<pk>\d+)$", views.EquipoDetalle.as_view(), name = "DetailEquipos"),
    path(r"^nuevo$", views.equipoFormulario, name= "NewEquipos"),
    path(r"^editar/(?P<pk>\d+)$", views.EquipoUpdate.as_view(), name= "EditEquipos"),
    path(r"^borrar/(?P<pk>\d+)$", views.EquipoDelete.as_view(), name="DeleteEquipos"),

    path("musico/lista", views.MusicoList.as_view(), name= "ListMusicos"),
    #path(r"^(?P<pk>\d+)$", views.MusicoDetalle.as_view(), name = "DetailMusicos"), no funciono
    path(r"nuevo_musico", views.MusicoCreacion.as_view(), name= "NewMusicos"),
    path(r"editar_musico/<pk>", views.MusicoUpdate.as_view(), name= "EditMusicos"),
    path(r"borrar_musico/<pk>", views.MusicoDelete.as_view(), name="DeleteMusicos"),
    
    path("login/", views.login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="AppFamilia/logout.html"), name="logout"),
    path("register/", views.register, name= "register"),
    path("editarUsuario/", views.editarUsuario, name="EditarUsuario"),

    path("about/", views.about, name="About"),


]