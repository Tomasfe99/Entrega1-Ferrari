from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
import datetime

def titulo(request):
    return HttpResponse("Este es mi primer MVT")

def mitemplate(request):
    nom= "Tomas"
    ape= "Ferrari"
    dia= datetime.datetime.now()

    diccionario = {"nombre": nom, "apellido": ape, "hoy": dia}
   
    miHtml= open("C:/Users/Usuario/Documents/Curso Python CH/mvtFerrariTomas/Plantillas/template.html")
    plantilla= Template(miHtml.read())
    miHtml.close()
    miContexto= Context(diccionario)
    documento= plantilla.render(miContexto)

    return HttpResponse(documento)
