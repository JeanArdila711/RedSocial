from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleoForm, VideoPostEmpleo_form
from .models import Empleo, VideoPostEmpleo
from users.models import Reclutador_empresa, Aspirante, IdiomaAspirante
from buscador_aspirante.models import Postulacion


def crear_empleo(request):
    reclutador = Reclutador_empresa.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = EmpleoForm(request.POST, request.FILES)
        if form.is_valid():
            empleo = form.save(commit=False)
            empleo.reclutador = reclutador  # Asigna el reclutador actual
            empleo.save()
            return redirect('mis_empleos')  # Redirigir a la lista de empleos o a donde prefieras
    else:
        form = EmpleoForm()

    return render(request, 'crear_empleo.html', {'form': form})


def mis_empleos(request):
    reclutador = Reclutador_empresa.objects.get(usuario=request.user)
    empleos = Empleo.objects.filter(reclutador=reclutador)

    return render(request, 'mis_empleos.html', {'empleos': empleos})


def detalle_empleo(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    videos_empleo = VideoPostEmpleo.objects.filter(empleo=empleo)  # Asegúrate de usar .objects

    return render(request, 'detalle_empleo.html', {'empleo': empleo, 'videos_empleo': videos_empleo})


def editar_empleo(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)

    reclutador = Reclutador_empresa.objects.get(usuario=request.user)

    # Verifica que el reclutador es el dueño del empleo

    if empleo.reclutador != reclutador:
        return redirect('mis_empleos')

    if request.method == 'POST':
        form = EmpleoForm(request.POST, request.FILES, instance=empleo)
        if form.is_valid():
            form.save()
            return redirect('detalle_empleo', empleo_id=empleo.id)
    else:
        form = EmpleoForm(instance=empleo)

    return render(request, 'editar_empleo.html', {'form': form, 'empleo': empleo})


def eliminar_empleo(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)

    # Verifica que el reclutador es el dueño del empleo
    reclutador = Reclutador_empresa.objects.get(usuario=request.user)

    if empleo.reclutador != reclutador:
        return redirect('mis_empleos')

    if request.method == 'POST':
        empleo.delete()
        return redirect('mis_empleos')

    return render(request, 'eliminar_empleo.html', {'empleo': empleo})


def cargar_video_post_empleo(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    if request.method == 'POST':
        form = VideoPostEmpleo_form(request.POST, request.FILES)
        if form.is_valid():
            video_post = form.save(commit=False)
            video_post.empleo = empleo  # Asignar el usuario actual
            video_post.save()
            return redirect('home_empresa')  # Redirigir a la lista de videos
    else:
        form = VideoPostEmpleo_form()
    return render(request, 'cargar_video_post_empleo.html', {'form': form})


def eliminar_video(request, video_id):
    video = get_object_or_404(VideoPostEmpleo, id=video_id)
    video.delete()
    return redirect('detalle_empleo', empleo_id=video.empleo.id)


def editar_video(request, video_id):
    video = get_object_or_404(VideoPostEmpleo, id=video_id)
    if request.method == 'POST':
        form = VideoPostEmpleo_form(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('detalle_empleo', empleo_id=video.empleo.id)
    else:
        form = VideoPostEmpleo_form(instance=video)

    return render(request, 'editar_video.html', {'form': form, 'video': video})


def postulaciones_empleos_reclutador(request):
    reclutador = Reclutador_empresa.objects.get(usuario=request.user)
    empleos = Empleo.objects.filter(reclutador=reclutador)

    postulaciones_por_empleo = {}
    for empleo in empleos:
        postulaciones = Postulacion.objects.filter(empleo=empleo)
        postulaciones_por_empleo[empleo] = postulaciones

    context = {
        'postulaciones_por_empleo': postulaciones_por_empleo,
    }
    return render(request, 'postulaciones_empleos_reclutador.html', context)


def perfil_aspirante(request, aspirante_id):
    aspirante = get_object_or_404(Aspirante, id=aspirante_id)
    idiomas = IdiomaAspirante.objects.filter(aspirante=aspirante)
    return render(request, 'base_ver_perfil_aspirante.html', {'aspirante': aspirante, 'idiomas': idiomas})

def ver_perfil_asociado_empleo(request, aspirante_id):
    aspirante = get_object_or_404(Aspirante, id=aspirante_id)
    idiomas = IdiomaAspirante.objects.filter(aspirante=aspirante)
    return render(request, 'ver_perfil_asociado_empleo.html', {'aspirante': aspirante, 'idiomas': idiomas})
