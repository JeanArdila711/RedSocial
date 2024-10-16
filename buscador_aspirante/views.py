from django.shortcuts import render, get_object_or_404, redirect
from empleos_reclutador.models import Empleo, VideoPostEmpleo
from users.models import Aspirante, Reclutador_empresa
from .models import Postulacion, Favoritos, Video_post
from django.contrib import messages
from .forms import CrearVideoForm
import numpy as np
import json
# Create your views here.


def detalle_empleo_aspirante(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    return render(request, 'detalle_empleo_aspirante.html', {'empleo': empleo})


def videos_empleos_disponibles(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    embedding_aspirante = np.array(json.loads(aspirante.embeddings)).flatten()
    empleos = Empleo.objects.all()
    resultados = []

    for empleo in empleos:
        embedding_empleo = np.array(json.loads(empleo.embeddings)).flatten()
        similitud = calcular_similitud(embedding_aspirante, embedding_empleo)
        videos_empleo = VideoPostEmpleo.objects.filter(empleo=empleo.id)
        resultados.append((empleo, similitud, videos_empleo))

    resultados.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'videos_empleos_disponibles.html', {'resultados': resultados})



def postularme_empleo(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    aspirante = Aspirante.objects.get(usuario=request.user)

    if Postulacion.objects.filter(aspirante=aspirante, empleo=empleo).exists():
        # Maneja el caso donde ya se ha postulado
        messages.warning(request, "Ya te has postulado para este empleo.")
        return redirect('detalle_empleo_aspirante', empleo_id=empleo.id)

    Postulacion.objects.create(aspirante=aspirante, empleo=empleo)
    messages.success(request, "¡Te has postulado correctamente para este empleo!")
    return redirect('detalle_empleo_aspirante', empleo_id=empleo.id)


def anadir_favoritos(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    aspirante = Aspirante.objects.get(usuario=request.user)
    if Favoritos.objects.filter(aspirante=aspirante, empleo=empleo).exists():
        messages.warning(request, "Ya te anadiste el empleo a favoritos.")
        return redirect('detalle_empleo_aspirante', empleo_id=empleo.id)

    Favoritos.objects.create(aspirante=aspirante, empleo=empleo)
    messages.success(request, "¡Anadiste correctamente a favoritos este empleo!")
    return redirect('detalle_empleo_aspirante', empleo_id=empleo.id)


def ver_mis_postulaciones(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    postulaciones = Postulacion.objects.filter(aspirante=aspirante)
    return render(request, 'mis_postulaciones.html', {'postulaciones': postulaciones})


def empleos_favoritos(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    favoritos = Favoritos.objects.filter(aspirante=aspirante)
    return render(request, 'empleos_favoritos.html', {'favoritos': favoritos})


def crear_video_post(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    if request.method == 'POST':
        video_post_form = CrearVideoForm(request.POST, request.FILES)
        if video_post_form.is_valid():
            video_post = video_post_form.save(commit=False)
            video_post.aspirante = aspirante
            video_post.save()
            return redirect('mis_videos_posts')
    else:
        video_post_form = CrearVideoForm()

        return render(request, 'crear_video_post.html', {'video_post_form': video_post_form})


def mis_videos_posts(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    videos = Video_post.objects.filter(aspirante=aspirante)
    return render(request, 'mis_videos_posts.html', {'videos': videos})


def editar_video(request, video_id):
    video = get_object_or_404(Video_post, id=video_id, aspirante__usuario=request.user)
    if request.method == 'POST':
        video.titulo = request.POST.get('titulo')
        video.descripcion = request.POST.get('descripcion')
        if 'video_post' in request.FILES:
            video.video_post = request.FILES['video_post']
        video.save()
        messages.success(request, 'El video se ha actualizado correctamente.')
        return redirect('mis_videos_posts')

    return render(request, 'editar_video_aspirante.html', {'video': video})


def eliminar_video(request, video_id):
    video = get_object_or_404(Video_post, id=video_id, aspirante__usuario=request.user)
    if request.method == 'POST':
        video.delete()
        messages.warning(request, 'El video ha sido eliminado correctamente.')
        return redirect('mis_videos_posts')
    return render(request, 'mis_videos_posts')


def empresas_aspirante(request):
    empresas = Reclutador_empresa.objects.all()
    return render(request, 'empresas_aspirante.html', {'empresas': empresas})


def calcular_similitud(embedding_aspirante, embedding_empleo):
    """Calcula la similitud coseno entre dos embeddings."""
    dot_product = np.dot(embedding_aspirante, embedding_empleo)
    norm_aspirante = np.linalg.norm(embedding_aspirante)
    norm_empleo = np.linalg.norm(embedding_empleo)
    return dot_product / (norm_aspirante * norm_empleo)


def empleos_aspirante(request, empresa_id=None):
    aspirante = Aspirante.objects.get(usuario=request.user)
    embedding_aspirante = np.array(json.loads(aspirante.embeddings)).flatten()
    if empresa_id:
        empleos = Empleo.objects.filter(reclutador=empresa_id)
        resultados = []

        for empleo in empleos:
            embedding_empleo = np.array(json.loads(empleo.embeddings)).flatten()
            similitud = calcular_similitud(embedding_aspirante, embedding_empleo)
            resultados.append((empleo, similitud))

        resultados.sort(key=lambda x: x[1], reverse=True)
    else:
        empleos = Empleo.objects.all()
        resultados = []

        for empleo in empleos:
            embedding_empleo = np.array(json.loads(empleo.embeddings)).flatten()
            similitud = calcular_similitud(embedding_aspirante, embedding_empleo)
            resultados.append((empleo, similitud))

        resultados.sort(key=lambda x: x[1], reverse=True)

    return render(request, 'empleos_aspirante.html', {
        'resultados': resultados,
    })
