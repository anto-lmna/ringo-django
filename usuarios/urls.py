from django.urls import path
from .views import (
    HomeView,
    PerfilCreateView,
    PerfilDetailView,
    PerfilUpdateView,
    PerfilDeleteView,
    MiembrosPanelView,
    perfil_redireccion,
    login_redireccion,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("perfil/redireccion", perfil_redireccion, name="perfil_redireccion"),
    path("login/redireccion/", login_redireccion, name="login_redireccion"),
    path("perfil/crear", PerfilCreateView.as_view(), name="crear_perfil"),
    path("perfil/<int:pk>/", PerfilDetailView.as_view(), name="ver_perfil"),
    path("perfil/editar/<int:pk>/", PerfilUpdateView.as_view(), name="editar_perfil"),
    path(
        "perfil/eliminar/<int:pk>/", PerfilDeleteView.as_view(), name="eliminar_perfil"
    ),
    path("miembros/", MiembrosPanelView.as_view(), name="miembros_panel"),
]
