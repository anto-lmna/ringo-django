from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Perfil
from .forms import PerfilForm


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

            # Verificar si el usuario pertenece al grupo 'Miembro'
            es_miembro = self.request.user.groups.filter(name="Miembro").exists()
            context["es_miembro"] = es_miembro

        return context


# Clase para saber si pertenece al grupo Miembro
class EsMiembroMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["es_miembro"] = self.request.user.groups.filter(
                name="Miembro"
            ).exists()
        return context


# Crear Perfil
class PerfilCreateView(LoginRequiredMixin, EsMiembroMixin, CreateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "perfil/perfil_form.html"

    def get_success_url(self):
        return reverse("ver_perfil", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Ver Perfil
class PerfilDetailView(LoginRequiredMixin, EsMiembroMixin, DetailView):
    model = Perfil
    template_name = "perfil/perfil_detail.html"
    context_object_name = "perfil"


# Editar Perfil
class PerfilUpdateView(LoginRequiredMixin, EsMiembroMixin, UpdateView):
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


# Redirecciona dependiendo de si se tiene perfil o no
def perfil_redireccion(request):
    if request.user.is_authenticated:
        try:
            perfil = Perfil.objects.get(user=request.user)
            return redirect("ver_perfil", pk=perfil.pk)
        except Perfil.DoesNotExist:
            return redirect("crear_perfil")
    else:
        return redirect("login")


@login_required
def login_redireccion(request):
    if request.user.is_superuser:
        return redirect("/admin")

    elif request.user.groups.filter(name="Miembro").exists():
        return redirect("home")
    else:
        try:
            perfil = Perfil.objects.get(user=request.user)
            return redirect("home")
        except Perfil.DoesNotExist:
            return redirect("crear_perfil")


# Panel visible para los del grupo Miembro
class MiembrosPanelView(LoginRequiredMixin, ListView):
    model = User
    template_name = "perfil/miembros_panel.html"
    context_object_name = "usuarios"
    paginate_by = 12

    def get_queryset(self):
        # Obtener usuarios junto con sus perfiles
        queryset = User.objects.all().select_related("perfil")

        # Filtrar por búsqueda si existe
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(
                Q(username__icontains=search_query)  # Buscar en nombre de usuario
                | Q(
                    perfil__nombre_perfil__icontains=search_query
                )  # Buscar en nombre del perfil
                | Q(perfil__deporte__icontains=search_query)  # Buscar en deporte
            ).distinct()

        # Filtrar usuarios con perfil asociado
        queryset = queryset.filter(perfil__isnull=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Paginación manual
        usuarios = self.get_queryset()  # Obtén el queryset de usuarios filtrados
        paginator = Paginator(usuarios, self.paginate_by)  # Paginar los resultados
        page = self.request.GET.get("page")  # Obtener el número de página de la URL

        try:
            usuarios = paginator.page(page)  # Obtener la página solicitada
        except PageNotAnInteger:
            # Si no es un número entero, mostramos la primera página
            usuarios = paginator.page(1)
        except EmptyPage:
            # Si la página está fuera de rango, mostramos la última página
            usuarios = paginator.page(paginator.num_pages)

        # Pasamos el queryset paginado al contexto
        context["usuarios"] = usuarios

        # Acceso al perfil del usuario logueado con manejo de excepción si no existe
        try:
            context["perfil"] = Perfil.objects.get(user=self.request.user)
        except Perfil.DoesNotExist:
            context["perfil"] = None

        return context
