from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_empleo/', views.crear_empleo, name='crear_empleo'),
    path('mis_empleos/', views.mis_empleos, name='mis_empleos'),
    path('empleo/<int:empleo_id>/', views.detalle_empleo, name='detalle_empleo'),
    path('empleo/<int:empleo_id>/editar/', views.editar_empleo, name='editar_empleo'),
    path('empleo/<int:empleo_id>/eliminar/', views.eliminar_empleo, name='eliminar_empleo'),
    path('empleo/<int:empleo_id>/cargar-video-post-empleo', views.cargar_video_post_empleo, name='cargar_video_post_empleo'),
    path('videos/editar/<int:video_id>/', views.editar_video, name='editar_video'),
    path('videos/eliminar/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
    path('postulaciones-empleos-reclutador/', views.postulaciones_empleos_reclutador, name='postulaciones_empleos_reclutador'),
    path('base-ver-perfil-aspirante/<int:aspirante_id>', views.perfil_aspirante, name='base_ver_perfil_aspirante'),
    path('ver-perfil-asociado-empleo/<int:aspirante_id>', views.ver_perfil_asociado_empleo, name='ver_perfil_asociado_empleo'),
]
