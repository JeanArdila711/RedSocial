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
    path('editar-perfil-reclutador/', views.editar_perfil_reclutador, name='editar_perfil_reclutador'),
    path('editar-perfil-aspirante/', views.editar_perfil_aspirante, name='editar_perfil_aspirante'),
    path('mi-perfil-reclutador/', views.mi_perfil_reclutador, name='mi_perfil_reclutador'),

]
