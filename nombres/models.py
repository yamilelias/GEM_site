from __future__ import unicode_literals

from django.db import models

class Nombre(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField()

    def __str__(self):
        return self.nombre

# Create your models here.
