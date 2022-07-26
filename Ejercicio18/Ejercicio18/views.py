from django.http import HttpResponse
from django.shortcuts import render

from Ejercicio18.models import Perfil


def Perfiles(request):
    users1 = Perfil.objects.create(name="Pedro", wager=75000, creation_date=25/7/2022)
    users2 = Perfil.objects.create(name="Juan", wager=50000, creation_date=25/7/2022)
    users3 = Perfil.objects.create(name="Jose", wager=79000, creation_date=25/7/2022)
    return render(request, "MVT.html", context= [users1, users2, users3])
