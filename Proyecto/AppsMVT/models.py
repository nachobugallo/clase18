from datetime import datetime
from django.db import models

class Perfil(models.Model):
    name = models.CharField(max_length=150)
    wager = models.FloatField()
    creation_date = models.DateField(datetime)