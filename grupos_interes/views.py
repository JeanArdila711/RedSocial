from django.shortcuts import render, redirect, get_object_or_404
from users.models import User, Aspirante, Reclutador_empresa
from .forms import PublicacionForm, ComentarioForm, GrupoInteresForm
from .models import GrupoInteres, Publicacion


def mis_grupos(request):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    grupos = GrupoInteres.objects.filter(miembros=user)
    print(grupos)  # Esto te ayudará a verificar qué grupos se están obteniendo
    return render(request, 'mis_grupos.html', {'grupos': grupos, 'base': base})


def crear_grupo(request):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    if request.method == 'POST':
        form = GrupoInteresForm(request.POST, request.FILES)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.creador = user
            grupo = form.save()
            grupo.miembros.add(user)

            return redirect('mis_grupos')
    else:
        form = GrupoInteresForm()

    return render(request, 'crear_grupo.html', {'form': form, 'base': base})


def detalle_grupo(request, grupo_interes_id):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    grupo = get_object_or_404(GrupoInteres, id=grupo_interes_id)
    miembros = grupo.miembros.all()
    return render(request, 'detalle_grupo.html', {'base': base, 'grupo': grupo, 'miembros': miembros})


def crear_publicacion_grupo(request, grupo_interes_id):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.grupo = get_object_or_404(Publicacion, id=grupo_interes_id)
            publicacion.autor = user
            publicacion = form.save()
            return redirect('mis_grupos')
    else:
        form = PublicacionForm()

    return render(request, 'crear_publicacion_grupo.html', {'form': form, 'base': base})


def publicaciones_grupo(request, grupo_interes_id):
    user = request.user
    grupo = get_object_or_404(GrupoInteres, id=grupo_interes_id)
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    publicaciones = Publicacion.objects.filter(grupo=grupo)

    return render(request, 'publicaciones_grupo.html', {'publicaciones': publicaciones, 'base': base})


def anadir_comentario(request, publicacion_id):
    user = request.user
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    grupo_interes_id = publicacion.grupo.id  # Asume que la publicación tiene una relación con GrupoInteres

    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador'):
        base = 'base_reclutador.html'

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = user
            comentario = form.save()
            publicacion.comentarios.add(comentario)
            return redirect('publicaciones', grupo_interes_id=grupo_interes_id)
    else:
        form = ComentarioForm()

    return render(request, 'anadir_comentario_grupo.html', {'form': form, 'base': base})



