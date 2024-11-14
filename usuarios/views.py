from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
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


class HomeView(TemplateView):
    template_name = "home.html"


# Crear Perfil
class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil_form.html"
    success_url = reverse_lazy("ver_perfil")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Ver Perfil
class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "perfil_detail.html"
    context_object_name = "perfil"


# Editar Perfil
class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil_form.html"
    success_url = reverse_lazy("ver_perfil")


# Eliminar Perfil
class PerfilDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "perfil_confirm_delete.html"
    success_url = reverse_lazy("perfil_list")
