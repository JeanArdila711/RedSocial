from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Aspirante, Reclutador_empresa, SectoresLaborales
from buscador_aspirante.models import Video_post, Favoritos
import numpy as np
import json
from django.db.models import Count, Avg
from django.conf import settings
from users.models import User


@login_required
def toggle_like_video_post_aspirante(request, video_post_aspirante_id):
    # Obtiene la publicación por ID o devuelve 404 si no existe
    VideoPost = get_object_or_404(Video_post, id=video_post_aspirante_id)

    # Verifica si el usuario actual ya ha dado "me gusta" a la publicación
    if request.user in VideoPost.likes.all():
        # Si el usuario ya ha dado like, lo quitamos
        VideoPost.likes.remove(request.user)
    else:
        # Si el usuario no ha dado like, lo añadimos
        VideoPost.likes.add(request.user)

    return redirect(request.META.get('HTTP_REFERER'))

# Create your views here.

def perfiles_aspirantes(request):
    reclutador_empresa = Reclutador_empresa.objects.get(usuario=request.user)
    embedding_empresa = np.array(json.loads(reclutador_empresa.embeddings)).flatten()

    # datos para la grafica de interes
    num_favoritos = Favoritos.objects.filter(empleo__reclutador=reclutador_empresa).count()
    num_aspirantes = Aspirante.objects.count()

    # Modalidades de trabajo
    conteo_por_modalidad = Aspirante.objects.values('modalidad_trabajo').annotate(total=Count('modalidad_trabajo'))
    modalidades = [modalidad['modalidad_trabajo'] for modalidad in conteo_por_modalidad]
    valores = [modalidad['total'] for modalidad in conteo_por_modalidad]


    aspirantes_all = Aspirante.objects.all()
    aspirantes = []

    # datos para la grafica de salario deseado del mercado
    currency_rates = settings.CURRENCY_RATES
    # Calcula los salarios en COP para cada aspirante
    salarios_por_sector = {}

    for aspirante in aspirantes_all:
        # Convierte el salario a COP
        tasa_cambio = currency_rates.get(aspirante.salario.currency, 1)
        salario_cop = aspirante.salario.amount * tasa_cambio

        # Agrega el salario convertido al sector correspondiente
        sector = aspirante.sector_laboral
        if sector not in salarios_por_sector:
            salarios_por_sector[sector] = []
        salarios_por_sector[sector].append(salario_cop)

    # Calcula el promedio de salario para cada sector
    promedio_por_sector = {
        sector: sum(salarios) / len(salarios) if salarios else 0
        for sector, salarios in salarios_por_sector.items()
    }

    # Prepara datos para la gráfica
    sectores_sal = [SectoresLaborales(sector).label for sector in promedio_por_sector.keys()]
    salarios_decimal_type = list(promedio_por_sector.values())
    salarios = [int(sal) for sal in salarios_decimal_type]



    for aspirante in aspirantes_all:
        aspirante_embedding = np.array(json.loads(aspirante.embeddings))
        similitud = calcular_similitud(embedding_empresa, aspirante_embedding)
        aspirantes.append((aspirante, similitud))

    aspirantes.sort(key=lambda x: x[1], reverse=True)

    # datos para la grafica de sectores laborales
    sectores = Aspirante.objects.values('sector_laboral').annotate(total=Count('sector_laboral')).order_by('-total')

    labels = [sector['sector_laboral'] for sector in sectores]
    data = [sector['total'] for sector in sectores]

    return render(request, 'perfiles_aspirantes.html', {'aspirantes': aspirantes, 'num_favoritos': num_favoritos, 'num_aspirantes': num_aspirantes, 'labels': labels,
     'data': data, 'sectores': sectores_sal, 'salarios': salarios, 'modalidades': modalidades, 'valores': valores})


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
