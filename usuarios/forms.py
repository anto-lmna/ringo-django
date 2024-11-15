from django import forms
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            "nombre_perfil",
            "fecha_nacimiento",
            "peso",
            "deporte",
            "genero",
            "foto",
        ]
        widgets = {
            "fecha_nacimiento": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "genero": forms.Select(attrs={"class": "form-control"}),
            "deporte": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
