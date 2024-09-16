from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('registrar-aspirante/', views.registrar_aspirante, name='register_aspirante'),
    path('registrar-reclutador/', views.registrar_reclutador, name='register_empresa'),
    path('completar-detalles/<int:aspirante_id>/', views.completar_detalles, name='completar_detalles'),
    path('login/', views.login_view, name='login'),
    path('home-aspirante/', views.home_aspirante, name='home_aspirante'),
    path('home-reclutador/', views.home_reclutador, name='home_reclutador'),
]
