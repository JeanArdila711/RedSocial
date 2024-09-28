from django.shortcuts import render
from users.models import Aspirante
# Create your views here.

def perfiles_aspirantes(request):
    # implementar sistema de busqueda de filtros basico, y sitema con IA
    aspirantes = Aspirante.objects.all()
    return render(request, 'perfiles_aspirantes.html', {'aspirantes': aspirantes})

