from django.shortcuts import render
from users.models import Aspirante
from buscador_aspirante.models import Video_post
# Create your views here.

def perfiles_aspirantes(request):
    # implementar sistema de busqueda de filtros basico, y sitema con IA
    aspirantes = Aspirante.objects.all()
    return render(request, 'perfiles_aspirantes.html', {'aspirantes': aspirantes})


def videos_aspirantes_disponibles(request):
    videos = Video_post.objects.all()
    return render(request, 'videos_aspirantes_disponibles.html', {'videos': videos})
