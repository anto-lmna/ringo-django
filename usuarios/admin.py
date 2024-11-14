from django.contrib import admin
from .models import Perfil
from django.utils.translation import gettext_lazy as _


# Registrar el modelo Perfil en el admin
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    verbose_name = _("Perfil")
    verbose_name_plural = _("Perfiles")

    list_display = (
        "nombre_perfil",
        "user",
        "fecha_nacimiento",
        "peso",
        "deporte",
        "genero",
    )  # Ajusta estos campos según los que quieras mostrar
    search_fields = (
        "nombre_perfil",
        "user__username",
    )  # Para permitir la búsqueda por nombre de perfil y usuario
    list_filter = ("deporte", "genero")  # Para agregar filtros por deporte y género
    readonly_fields = ("user",)  # Si quieres que el campo 'user' sea solo lectura
