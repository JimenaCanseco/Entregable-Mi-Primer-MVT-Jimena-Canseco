from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludar(request):
    return HttpResponse("Hola!!")

def presentacion(request):
    return HttpResponse("Este es mi ejercicio entregable : Mi primer MVT")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena=f"Hoy es {dia}"
    return HttpResponse(cadena)

'''def probandohtml(request):

    diccionario={"Familia_Argento":[ "Padre: José Argento, edad: 67 años" , " Madre: Mónica Argento, edad: 48 años" , "Hijo: Alfio Argento, edad: 21", "Hija: Paola Argento, edad: 18 años"]}

    archivo=open("C:/Users/Dell/Documents/Python/EntregableMVT/Plantillas/Template.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)

    documento=template.render(contexto)
    return HttpResponse(documento)'''

def probandohtml(request):

    diccionario={"Familia_Argento":[ "Padre: José Argento, edad: 67 años" , " Madre: Mónica Argento, edad: 48 años" , "Hijo: Alfio Argento, edad: 21", "Hija: Paola Argento, edad: 18 años"]}

    template=loader.get_template("Template.html")

    documento=template.render(diccionario)
    return HttpResponse(documento)