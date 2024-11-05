from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_empleo/', views.crear_empleo, name='crear_empleo'),
    path('mis_empleos/', views.mis_empleos, name='mis_empleos'),
    path('empleo/<int:empleo_id>/', views.detalle_empleo, name='detalle_empleo'),
    path('empleo/<int:empleo_id>/editar/', views.editar_empleo, name='editar_empleo'),
    path('empleo/<int:empleo_id>/eliminar/', views.eliminar_empleo, name='eliminar_empleo'),
    path('empleo/<int:empleo_id>/cargar-video-post-empleo', views.cargar_video_post_empleo, name='cargar_video_post_empleo'),
    path('videos/editar/empresa/<int:video_id>/', views.editar_video_reclutador, name='editar_video_reclutador'),
    path('videos/eliminar/empresa/<int:video_id>/', views.eliminar_video_reclutador, name='eliminar_video_reclutador'),
    path('postulaciones-empleos-reclutador/', views.postulaciones_empleos_reclutador, name='postulaciones_empleos_reclutador'),
    path('base-ver-perfil-aspirante/<int:aspirante_id>', views.perfil_aspirante, name='base_ver_perfil_aspirante'),
    path('enviar-oferta/<int:aspirante_id>', views.enviar_oferta, name='enviar_oferta'),
]
