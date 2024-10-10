from django.urls import path
from . import views  # Importas las vistas de tu aplicación

urlpatterns = [
    path('perfiles_aspirantes/', views.perfiles_aspirantes, name='perfiles_aspirantes'),
    path('videos_aspirantes_disponibles/', views.videos_aspirantes_disponibles, name='videos_aspirantes_disponibles'),

]
