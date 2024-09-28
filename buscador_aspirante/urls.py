from django.urls import path, include
from . import views

urlpatterns = [
    path('empleos-aspirante/', views.empleos_aspirante, name='empleos_aspirante'),
    path('empleo-aspirante/<int:empleo_id>/', views.detalle_empleo_aspirante, name='detalle_empleo_aspirante'),

]
