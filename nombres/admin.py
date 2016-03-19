from django.contrib import admin
from models import Nombre

admin.site.register(Nombre)
# Register your models here.

nombre = Nombre.objects.get(pk=1)
