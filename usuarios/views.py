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


# Home
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            try:
                perfil = self.request.user.perfil
            except Perfil.DoesNotExist:
                perfil = None
            context["perfil"] = perfil

        return context


# Crear Perfil
class PerfilCreateView(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil/perfil_form.html"

    def get_success_url(self):
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

    def get_success_url(self):
        return reverse("ver_perfil", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        if not form.cleaned_data["foto"]:
            form.cleaned_data["foto"] = self.object.foto

            # Si no se proporciona una nueva fecha, conservar la actual
        if not form.cleaned_data.get("fecha_nacimiento"):
            form.instance.fecha_nacimiento = self.object.fecha_nacimiento

        return super().form_valid(form)


# Eliminar Perfil
class PerfilDeleteView(LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "perfil/perfil_confirm_delete.html"
    success_url = reverse_lazy("crear_perfil")


def perfil_redireccion(request):
    if request.user.is_authenticated:
        try:
            perfil = Perfil.objects.get(user=request.user)
            return redirect("ver_perfil", pk=perfil.pk)
        except Perfil.DoesNotExist:
            return redirect("crear_perfil")
    else:
        return redirect("login")
