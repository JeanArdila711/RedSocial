from django.shortcuts import render
from users.models import Aspirante, Reclutador_empresa
from buscador_aspirante.models import Video_post
import numpy as np
import json
# Create your views here.

def perfiles_aspirantes(request):
    reclutador_empresa = Reclutador_empresa.objects.get(usuario=request.user)
    embedding_empresa = np.array(json.loads(reclutador_empresa.embeddings)).flatten()

    aspirantes_all = Aspirante.objects.all()
    aspirantes = []

    for aspirante in aspirantes_all:
        aspirante_embedding = np.array(json.loads(aspirante.embeddings))
        similitud = calcular_similitud(embedding_empresa, aspirante_embedding)
        aspirantes.append((aspirante, similitud))

    aspirantes.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'perfiles_aspirantes.html', {'aspirantes': aspirantes})


def videos_aspirantes_disponibles(request):
    reclutador_empresa = Reclutador_empresa.objects.get(usuario=request.user)
    embedding_empresa = np.array(json.loads(reclutador_empresa.embeddings)).flatten()
    videos_posts = Video_post.objects.all()
    videos = []

    for video in videos_posts:
        video_embedding = np.array(json.loads(video.embeddings))
        similitud = calcular_similitud(embedding_empresa, video_embedding)
        videos.append((video, similitud))

    videos.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'videos_aspirantes_disponibles.html', {'videos': videos})


def calcular_similitud(embedding_aspirante, embedding_empleo):
    """Calcula la similitud coseno entre dos embeddings."""
    dot_product = np.dot(embedding_aspirante, embedding_empleo)
    norm_aspirante = np.linalg.norm(embedding_aspirante)
    norm_empleo = np.linalg.norm(embedding_empleo)
    return dot_product / (norm_aspirante * norm_empleo)
