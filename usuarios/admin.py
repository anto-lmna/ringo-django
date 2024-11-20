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
    )  # campos que se muestran
    search_fields = (
        "nombre_perfil",
        "user__username",
    )  # busqueda por perfil y usuario
    list_filter = ("deporte", "genero")  # filtra por deporte y genero
    readonly_fields = ("user",)  # Campo user solo de lectura
