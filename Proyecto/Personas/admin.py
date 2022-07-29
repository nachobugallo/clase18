from django.contrib import admin
from Personas.models import Perfil
# Register your models here.
@admin.register(Perfil)
class Perfil_admin(admin.ModelAdmin):
    list_display = ['name', 'wager', 'creation_date']
