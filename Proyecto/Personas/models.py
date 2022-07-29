from datetime import datetime
from django.db import models

class Perfil(models.Model):
    name = models.CharField(max_length=150)
    wager = models.FloatField()
    creation_date = models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"