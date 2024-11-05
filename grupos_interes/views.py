from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from users.models import User, Aspirante, Reclutador_empresa
from .forms import PublicacionForm, ComentarioForm, GrupoInteresForm
from .models import GrupoInteres, Publicacion


def mis_grupos(request):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador_empresa'):
        base = 'base_reclutador.html'

    print(f'holaa{base}')
    grupos = GrupoInteres.objects.filter(miembros=user)

    return render(request, 'mis_grupos.html', {'grupos': grupos, 'base': base})


def crear_grupo(request):
    user = request.user
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador_empresa'):
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

    if hasattr(user, 'reclutador_empresa'):
        base = 'base_reclutador.html'

    grupo = get_object_or_404(GrupoInteres, id=grupo_interes_id)
    miembros = grupo.miembros.all()
    return render(request, 'detalle_grupo.html', {'base': base, 'grupo': grupo, 'miembros': miembros})


def crear_publicacion_grupo(request, grupo_interes_id):
    user = request.user
    grupo = get_object_or_404(GrupoInteres, id=grupo_interes_id)
    nombre_grupo = grupo.nombre

    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador_empresa'):
        base = 'base_reclutador.html'

    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.grupo = grupo
            publicacion.autor = user
            publicacion = form.save()
            return redirect('mis_grupos')
    else:
        form = PublicacionForm()

    return render(request, 'crear_publicacion_grupo.html', {'form': form, 'base': base, 'nombre_grupo': nombre_grupo})


def publicaciones_grupo(request, grupo_interes_id):
    user = request.user
    grupo = get_object_or_404(GrupoInteres, id=grupo_interes_id)
    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador_empresa'):
        base = 'base_reclutador.html'

    publicaciones = Publicacion.objects.filter(grupo=grupo)
    nombre_grupo = grupo.nombre

    return render(request, 'publicaciones_grupo.html', {'publicaciones': publicaciones, 'base': base, 'nombre_grupo': nombre_grupo})


def anadir_comentario_grupo(request, publicacion_id):
    user = request.user
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    grupo_interes_id = publicacion.grupo.id  # Asume que la publicación tiene una relación con GrupoInteres

    base = ''
    if hasattr(user, 'aspirante'):
        base = 'base_aspirante.html'

    if hasattr(user, 'reclutador_empresa'):
        base = 'base_reclutador.html'

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = user
            comentario = form.save()
            publicacion.comentarios.add(comentario)
            return redirect('publicaciones_grupo', grupo_interes_id)
    else:
        form = ComentarioForm()

    return render(request, 'anadir_comentario_grupo.html', {'form': form, 'base': base, 'publicacion': publicacion_id})


@login_required
def toggle_like_publicacion(request, publicacion_id):
    # Obtiene la publicación por ID o devuelve 404 si no existe
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)

    # Verifica si el usuario actual ya ha dado "me gusta" a la publicación
    if request.user in publicacion.likes.all():
        # Si el usuario ya ha dado like, lo quitamos
        publicacion.likes.remove(request.user)
    else:
        # Si el usuario no ha dado like, lo añadimos
        publicacion.likes.add(request.user)

    # Redirige a la página anterior o a la lista de publicaciones
    return redirect(request.META.get('HTTP_REFERER'))
