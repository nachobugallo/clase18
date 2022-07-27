from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)