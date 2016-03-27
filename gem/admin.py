from django.contrib import admin
from gem.models import GrupoEstudiantil, Evento, Asistencia, Usuario
from django.contrib.auth.models import Group, User, Permission

for user in User.objects.all():
    add_evento = Permission.objects.get(codename='add_evento')
    change_evento = Permission.objects.get(codename='change_evento')
    delete_evento = Permission.objects.get(codename='delete_evento')
    add_asistencia = Permission.objects.get(codename='add_asistencia')
    change_asistencia = Permission.objects.get(codename='change_asistencia')
    delete_asistencia = Permission.objects.get(codename='delete_asistencia')
    add_usuario = Permission.objects.get(codename='add_usuario')
    change_usuario = Permission.objects.get(codename='change_usuario')
    delete_usuario = Permission.objects.get(codename='delete_usuario')
    change_grupo_estudiantil = Permission.objects.get(codename='change_grupoestudiantil')
    user.user_permissions.add(
        add_evento, change_evento, delete_evento,
        add_asistencia, change_asistencia, delete_asistencia,
        add_usuario, change_usuario, delete_usuario,
        change_grupo_estudiantil)


class UsuarioInline(admin.TabularInline):
    model = Usuario
    extra = 1

class AsistenciaInline(admin.TabularInline):
    model = Asistencia
    extra = 1

class AsistenciaAdmin(admin.ModelAdmin):
    inlines = [UsuarioInline]

class EventoAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'grupo_estudiantil', 'event_date')
    inlines = [AsistenciaInline]

    def get_queryset(self, request):
        qs = super(EventoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        #get the grupo estudiantil
        return qs.filter(grupo_estudiantil__owner__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'grupo_estudiantil' and not request.user.is_superuser:
            kwargs["queryset"] = GrupoEstudiantil.objects.filter(owner__in=request.user.groups.all())
            return db_field.formfield(**kwargs)
        return super(EventoAdmin,self).formfield_for_foreignkey(db_field, request, **kwargs)

class GrupoEstudiantilAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(GrupoEstudiantilAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # return qs.filter(grupo_estudiantil__owner__in=request.user.groups.all())
        return qs.filter(owner__in=request.user.groups.all())

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'owner' and not request.user.is_superuser:
            kwargs["queryset"] = Group.objects.filter(pk=request.user.groups.all())
            return db_field.formfield(**kwargs)
        return super(GrupoEstudiantilAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(GrupoEstudiantil, GrupoEstudiantilAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Usuario)