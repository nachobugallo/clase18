from django.http import HttpResponse
from django.shortcuts import render

from AppsMVT.models import Perfil


def Perfiles(request):
    users1 = Perfil.objects.create(name="Pedro", wager=75000, creation_date=("2002-9-22"))
    users2 = Perfil.objects.create(name="Juan", wager=50000, creation_date=("2005-9-15"))
    users3 = Perfil.objects.create(name="Jose", wager=79000, creation_date=("2012-3-5"))
    return render(request, "MVT.html", context= [users1, users2, users3])
