from django.urls import path, include
from . import views

urlpatterns = [
    path('detalle_empleo_aspirante/<int:empleo_id>/', views.detalle_empleo_aspirante, name='detalle_empleo_aspirante'),
    path('videos-empleos-disponibles/', views.videos_empleos_disponibles, name='videos_empleos_disponibles'),
    path('postularme-empleo/<int:empleo_id>/', views.postularme_empleo, name='postularme_empleo'),
    path('mis-postulaciones/', views.ver_mis_postulaciones, name='mis_postulaciones'),
    path('anadir-favoritos/<int:empleo_id>/', views.anadir_favoritos, name='anadir_favoritos'),
    path('empleos-favoritos/', views.empleos_favoritos, name='empleos_favoritos'),
    path('crear-video-post/', views.crear_video_post, name='crear_video_post'),
    path('mis-videos-posts', views.mis_videos_posts, name='mis_videos_posts'),
    path('editar-video/<int:video_id>/', views.editar_video, name='editar_video'),
    path('eliminar-video/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
    path('empresas_aspirante', views.empresas_aspirante, name='empresas_aspirante'),
    path('empleos_aspirante/', views.empleos_aspirante, name='empleos_aspirante'),
    path('empleos/<int:empresa_id>/', views.empleos_aspirante, name='empleos_aspirante'),

]
