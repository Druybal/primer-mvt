from unittest import loader
from django.shortcuts import render, HttpResponse
from django.template import loader,Context,Template
from Familiares.models import familiar

# Create your views here.
def listado_familiares(request):
    familiar1=familiar(nombre='Nicolas',parentesco='hermano',dni=30123456,fecha_nacimiento=11/8/1980)
    familiar1.save()

    familiar2=familiar(nombre='Carolina',parentesco='hermana',dni=31256987,fecha_nacimiento=25/10/1982)
    familiar2.save()

    familiar3=familiar(nombre='Roberto',parentesco='padre',dni=10235478,fecha_nacimiento=20/12/1956)
    familiar3.save()

    familiar4=familiar(nombre='Beatriz',parentesco='madre',dni=11247985,fecha_nacimiento=11/4/1950)
    familiar4.save()

    plantilla=loader.get_template('template.html')
    familia= {'familia':[familiar1,familiar2,familiar3,familiar4]}
    vista = plantilla.render(familia)    
    return HttpResponse(vista)




        