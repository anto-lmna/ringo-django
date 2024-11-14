from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Perfil
from .forms import PerfilForm
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = "home.html"


# Crear Perfil
class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil/perfil_form.html"

    def get_success_url(self):
        # El 'self.object' es el objeto de perfil creado, que tiene el 'pk' asignado después de guardarlo.
        return reverse("ver_perfil", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Ver Perfil
class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "perfil/perfil_detail.html"
    context_object_name = "perfil"


# Editar Perfil
class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil/perfil_form.html"
    success_url = reverse_lazy("ver_perfil")


# Eliminar Perfil
class PerfilDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "perfil/perfil_confirm_delete.html"
    success_url = reverse_lazy("crear_perfil")


def perfil_redireccion(request):
    if request.user.is_authenticated:
        try:
            # Verificar si el perfil del usuario existe
            perfil = Perfil.objects.get(user=request.user)
            return redirect("ver_perfil", pk=perfil.pk)
        except Perfil.DoesNotExist:
            # Redirigir a crear perfil si no existe
            return redirect("crear_perfil")
    else:
        # Si el usuario no está autenticado, redirigir al login
        return redirect("login")
