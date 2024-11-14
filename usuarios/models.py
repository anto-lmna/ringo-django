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
        max_length=10,
        choices=[
            ("masculino", "Masculino"),
            ("femenino", "Femenino"),
            ("otro", "Otro"),
        ],
        default="otro",
    )

    def __str__(self):
        return self.nombre_perfil

    def calcular_edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            edad = (
                today.year
                - self.fecha_nacimiento.year
                - (
                    (today.month, today.day)
                    < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
                )
            )
            return edad
        return None
