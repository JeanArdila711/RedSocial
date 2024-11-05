from django.urls import path
from . import views  # Importas las vistas de tu aplicación

urlpatterns = [
    path('perfiles_aspirantes/', views.perfiles_aspirantes, name='perfiles_aspirantes'),
    path('videos_aspirantes_disponibles/', views.videos_aspirantes_disponibles, name='videos_aspirantes_disponibles'),
    path('video_post_aspirante/<int:video_post_aspirante_id>/like/', views.toggle_like_video_post_aspirante,
         name='toggle_like_video_post_aspirante'),

]
