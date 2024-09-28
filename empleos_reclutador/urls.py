from django.urls import path, include
from . import views

urlpatterns = [
    path('crear_empleo/', views.crear_empleo, name='crear_empleo'),
    path('mis_empleos/', views.mis_empleos, name='mis_empleos'),
    path('empleo/<int:empleo_id>/', views.detalle_empleo, name='detalle_empleo'),
    path('empleo/<int:empleo_id>/editar/', views.editar_empleo, name='editar_empleo'),
    path('empleo/<int:empleo_id>/eliminar/', views.eliminar_empleo, name='eliminar_empleo'),

]
