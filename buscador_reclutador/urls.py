from django.urls import path
from . import views  # Importas las vistas de tu aplicación

urlpatterns = [
    path('perfiles_aspirantes/', views.perfiles_aspirantes, name='perfiles_aspirantes'),
]
