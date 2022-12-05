from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

# Create your views here.
def familia(request):

    integrante1= Familia(parentesco="Padre", nombre="José", apellido="Argento", edad=67, fecha_nacimiento= "14 de febrero 1955")
    integrante1.save()
    cadena_texto1=f"integrante 1: parentesco: {integrante1.parentesco}, nombre: {integrante1.nombre}, apellido: {integrante1.apellido}, edad: {integrante1.edad}, fecha de nacimiento {integrante1.fecha_nacimiento}"
    integrante2= Familia(parentesco="Madre", nombre="Mónica", apellido="Argento", edad=48, fecha_nacimiento= "7 de noviembre 1974")
    integrante2.save()
    cadena_texto2=f"integrante 2: parentesco: {integrante2.parentesco}, nombre: {integrante2.nombre}, apellido: {integrante2.apellido}, edad: {integrante2.edad}, fecha de nacimiento {integrante2.fecha_nacimiento}"
    integrante3= Familia(parentesco="Hijo", nombre="Alfio", apellido="Argento", edad=20, fecha_nacimiento= "29 de enero 2002")
    integrante3.save()
    cadena_texto3=f"integrante 3: parentesco: {integrante3.parentesco}, nombre: {integrante3.nombre}, apellido: {integrante3.apellido}, edad: {integrante3.edad}, fecha de nacimiento {integrante3.fecha_nacimiento}"
    integrante4= Familia(parentesco="Hija", nombre="Paola", apellido="Argento", edad=18, fecha_nacimiento= "1 de enero 2004")
    integrante4.save()
    cadena_texto4=f"integrante 4: parentesco: {integrante4.parentesco}, nombre: {integrante4.nombre}, apellido: {integrante4.apellido}, edad: {integrante4.edad}, fecha de nacimiento {integrante4.fecha_nacimiento}"
    
    return HttpResponse(cadena_texto1)
    return HttpResponse(cadena_texto2)
    return HttpResponse(cadena_texto3)
    return HttpResponse(cadena_texto4)