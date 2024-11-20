# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import date


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_perfil = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.1)],
        null=True,
        blank=True,
    )
    deporte = models.CharField(
        max_length=50, choices=[("boxeo", "Boxeo"), ("kickboxing", "Kickboxing")]
    )
    foto = models.ImageField(upload_to="perfil_fotos/", blank=True, null=True)
    genero = models.CharField(
        max_length=20,
        choices=[
            ("masculino", "Masculino"),
            ("femenino", "Femenino"),
            ("prefiero no decir", "Prefiero no decir"),
        ],
        default="otro",
    )

    def __str__(self):
        return self.nombre_perfil

    @property
    def edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            edad = today.year - self.fecha_nacimiento.year
            if today.month < self.fecha_nacimiento.month or (
                today.month == self.fecha_nacimiento.month
                and today.day < self.fecha_nacimiento.day
            ):
                edad -= 1
            return edad
        return None
