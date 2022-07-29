import imp
from multiprocessing import context
from django.shortcuts import render

from Personas.models import Perfil

def create_perfil (request):
    nuevo_perfil= Perfil.objects.create(name='Juan',wager=78000,creation_date='2020-3-25')
    context={
        'nuevo_perfil':nuevo_perfil
    }
    return render(request,'nuevo_perfil.html',context=context)

def lista_perfiles(request):
    nomina = Perfil.objects.all()
    context={
        'plantel': nomina
    }
    return render (request,'lista-perfil.html',context=context)

def introduccion(request):
    saludo = str("Bienvenido")
    context={'introduccion1':saludo}
    return render (request, 'inicio.html', context=context)