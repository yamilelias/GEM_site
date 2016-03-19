# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group, User


class GrupoEstudiantil(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField('Descripcion', default="Descripcion")
    owner = models.ForeignKey(Group)

    def __str__(self):
        return self.name

class Evento(models.Model):
    grupo_estudiantil = models.ForeignKey(GrupoEstudiantil)
    event_name = models.CharField(max_length=200, unique=True)
    description = models.TextField('Descripción')
    place = models.TextField(verbose_name='Lugar', max_length=500)
    event_date = models.DateTimeField('Fecha y hora')
    duration = models.CharField(max_length=200, verbose_name='Duración', blank=True, null=True)


class Usuario(models.Model):
    usuario_name = models.CharField(max_length=200, unique=False)
    usuario_apellido_paterno = models.CharField(max_length=200, unique=False)
    usuario_apellido_materno = models.CharField(max_length=200, unique=False, blank=True, null=True)

class Asistencia(models.Model):
    evento = models.ForeignKey(Evento)
    usuario_asistente = models.ForeignKey(Usuario)




# Create your models here.
