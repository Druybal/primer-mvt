from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.template import Template,Context
from Familiares.models import Familiar

# Create your views here.
def listado_familiares(request):
    familiar1=Familiar(nombre='Nicolas',parentesco='hermano',dni=30123456,fecha_nacimiento='1980-08-11')
    familiar1.save()

    familiar2=Familiar(nombre='Carolina',parentesco='hermana',dni=31256987,fecha_nacimiento='1980-10-25')
    familiar2.save()

    familiar3=Familiar(nombre='Roberto',parentesco='padre',dni=10235478,fecha_nacimiento='1956-12-20')
    familiar3.save()

    familiar4=Familiar(nombre='Beatriz',parentesco='madre',dni=11247985,fecha_nacimiento='1950-04-11')
    familiar4.save()

    plantilla=loader.get_template('template.html')
    familia= {'familia':[familiar1,familiar2,familiar3,familiar4]}
    vista = plantilla.render(familia)    
    return HttpResponse(vista)




        