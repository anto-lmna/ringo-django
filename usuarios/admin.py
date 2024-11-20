from django.contrib import admin
from .models import Perfil


# Registro del modelo Perfil en el admin
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    verbose_name = "Perfil"
    verbose_name_plural = "Perfiles"

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
    readonly_fields = ("user",)  # Campo user solo de lectura
