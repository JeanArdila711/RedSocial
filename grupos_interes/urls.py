from django.urls import path, include
from . import views
urlpatterns = [
    path('mis_grupos', views.mis_grupos, name='mis_grupos'),
    path('crear_grupo', views.crear_grupo, name='crear_grupo'),
    path('detalle_grupo/<int:grupo_interes_id>/', views.detalle_grupo, name='detalle_grupo'),
    path('crear_publicacion_grupo/<int:grupo_interes_id>/', views.crear_publicacion_grupo, name='crear_publicacion_grupo'),
    path('publicaciones_grupo/<int:grupo_interes_id>/', views.publicaciones_grupo, name='publicaciones_grupo'),
    path('anadir_comentario/<int:publicacion_id>/', views.anadir_comentario, name='anadir_comentario'),
]
