from django.urls import path, include
from . import views
urlpatterns = [
    path('mis_grupos', views.mis_grupos, name='mis_grupos'),
    path('crear_grupo', views.crear_grupo, name='crear_grupo'),
    path('detalle_grupo/<int:grupo_interes_id>/', views.detalle_grupo, name='detalle_grupo'),
    path('crear_publicacion_grupo/<int:grupo_interes_id>/', views.crear_publicacion_grupo, name='crear_publicacion_grupo'),
    path('publicaciones_grupo/<int:grupo_interes_id>/', views.publicaciones_grupo, name='publicaciones_grupo'),
    path('anadir_comentario_grupo/<int:publicacion_id>/', views.anadir_comentario_grupo, name='anadir_comentario_grupo'),
    path('publicacion/<int:publicacion_id>/like/', views.toggle_like_publicacion, name='toggle_like_publicacion'),

]
