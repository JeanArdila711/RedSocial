from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('registrar-aspirante/', views.registrar_aspirante, name='register_aspirante'),
    path('registrar-reclutador/', views.registrar_reclutador, name='register_empresa'),
    path('completar-detalles/<int:aspirante_id>/', views.completar_detalles, name='completar_detalles'),
    path('login/', views.login_view, name='login'),
    path('home-aspirante/', views.home_aspirante, name='home_aspirante'),
    path('home-empresa/', views.home_empresa, name='home_empresa'),
    path('editar-perfil-aspirante/', views.editar_perfil_aspirante, name='editar_perfil_aspirante'),
    path('mi-perfil-reclutador/', views.mi_perfil_reclutador, name='mi_perfil_reclutador'),
    path('editar-empresa/', views.editar_empresa, name='editar_empresa'),
    path('editar-reclutador/', views.editar_reclutador, name='editar_reclutador'),
    path('editar-representante-legal/', views.editar_representante_legal, name='editar_representante_legal'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('mi-perfil-aspirante/', views.mi_perfil_aspirante, name='mi_perfil_aspirante'),
    path('editar-aspirante-user/', views.editar_aspirante_user, name='editar_aspirante_user'),
    path('editar-aspirante-aspirante/', views.editar_aspirante_aspirante, name='editar_aspirante_aspirante'),
    path('agregar_formacion/', views.agregar_formacion, name='agregar_formacion'),
    path('agregar_experiencia/', views.agregar_experiencia, name='agregar_experiencia'),

]
