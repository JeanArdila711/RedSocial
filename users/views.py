from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, AspiranteCreationForm, ReclutadorCreationForm, RepresentanteLegalForm, IdiomaAspiranteForm, FormacionAspiranteForm, RedesSocialesForm, CustomUserForm_sin_contra, ExperienciaLaboralForm
from .models import Aspirante, Reclutador_empresa, RedesSociales, IdiomaAspirante, FormacionAspirante, ExperienciaLaboral
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from empleos_reclutador.models import Empleo, VideoPostEmpleo
import numpy as np
import json
from grupos_interes.models import GrupoInteres
from buscador_aspirante.models import Video_post

from django.contrib import messages



def registrar_aspirante(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES, prefix='user')
        aspirante_form = AspiranteCreationForm(request.POST, request.FILES)
        redes_sociales_form = RedesSocialesForm(request.POST, request.FILES, prefix='redes_sociales')
        idioma_form = IdiomaAspiranteForm(request.POST)

        if user_form.is_valid() and aspirante_form.is_valid() and redes_sociales_form.is_valid() and idioma_form.is_valid():
            user = user_form.save(commit=False)
            user.tipo_usuario = 'aspirante'  # Set the user type
            user.save()

            aspirante = aspirante_form.save(commit=False)
            redes_sociales = redes_sociales_form.save()
            aspirante.usuario = user
            aspirante.redes_sociales = redes_sociales
            aspirante.save()

            idiomas_seleccionados = idioma_form.cleaned_data['idiomas']
            for idioma in idiomas_seleccionados:
                IdiomaAspirante.objects.create(aspirante=aspirante, idioma=idioma)

            login(request, user)  # Auto-login after registration
            return redirect('completar_detalles', aspirante_id=aspirante.id)  # Redirect to a profile or another page
    else:
        user_form = CustomUserCreationForm(prefix='user')
        aspirante_form = AspiranteCreationForm()
        redes_sociales_form = RedesSocialesForm(prefix='redes_sociales')
        idioma_form = IdiomaAspiranteForm()  # Inicializar el formulario de idiomas

    return render(request, 'register_aspirante.html', {
        'user_form': user_form,
        'aspirante_form': aspirante_form,
        'redes_sociales_form': redes_sociales_form,  # Pasa el formulario al contexto
        'idioma_form': idioma_form,  # Pasar el formulario de idiomas al contexto

    })

def registrar_reclutador(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES, prefix='user')
        reclutador_form = ReclutadorCreationForm(request.POST, request.FILES, prefix='reclutador')
        representante_legal_form = RepresentanteLegalForm(request.POST, request.FILES, prefix='representante_legal')

        if user_form.is_valid() and representante_legal_form.is_valid() and reclutador_form.is_valid():
            user = user_form.save(commit=False)
            user.tipo_usuario = 'reclutador'  # Set the user type
            user.save()

            representante_legal = representante_legal_form.save()
            reclutador_empresa = reclutador_form.save(commit=False)
            reclutador_empresa.usuario = user
            reclutador_empresa.representante_legal = representante_legal
            reclutador_empresa.save()

            login(request, user)
            return redirect('home_empresa')
    else:
        user_form = CustomUserCreationForm(prefix='user')
        representante_legal_form = RepresentanteLegalForm(prefix='representante_legal')
        reclutador_form = ReclutadorCreationForm(prefix='reclutador')

    return render(request, 'register_empresa.html', {
        'user_form': user_form,
        'representante_legal_form': representante_legal_form,
        'reclutador_form': reclutador_form
    })


def completar_detalles(request, aspirante_id):
    aspirante = Aspirante.objects.get(id=aspirante_id)

    if request.method == 'POST':
        formacion_form = FormacionAspiranteForm(request.POST)

        if formacion_form.is_valid():
            formacion = formacion_form.save(commit=False)
            formacion.aspirante = aspirante
            formacion.save()

            if 'añadir mas' in request.POST:
                return redirect('completar_detalles', aspirante_id=aspirante_id)

            return redirect('completar_detalles_experiencia',  aspirante_id=aspirante_id)  # Redirect to a profile or another page

    else:
        formacion_form = FormacionAspiranteForm()

    return render(request, 'completar_detalles.html', {
        'formacion_form': formacion_form
    })


def completar_detalles_experiencia(request, aspirante_id):
    aspirante = Aspirante.objects.get(id=aspirante_id)

    if request.method == 'POST':
        experiencia_form = ExperienciaLaboralForm(request.POST)

        if experiencia_form.is_valid():
            experiencia = experiencia_form.save(commit=False)
            experiencia.aspirante = aspirante
            experiencia.save()

            if 'añadir mas' in request.POST:
                return redirect('completar_detalles_experiencia', aspirante_id=aspirante_id)

            return redirect('home_aspirante')  # Redirect to a profile or another page

    else:
        experiencia_form = ExperienciaLaboralForm()

    return render(request, 'completar_detalles_experiencia.html', {
        'experiencia_form': experiencia_form
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Redireccionar basado en el tipo de usuario
            if user.tipo_usuario == 'aspirante':
                return redirect('home_aspirante')
            elif user.tipo_usuario == 'reclutador':
                return redirect('home_empresa')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



@login_required
def home_aspirante(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    embedding_aspirante = np.array(json.loads(aspirante.embeddings)).flatten()
    empleos = Empleo.objects.all()
    empresas = Reclutador_empresa.objects.all()
    grupos = GrupoInteres.objects.all()
    resultados = []
    resultados_empresas = []
    resultados_grupos = []
    resultados_video_post = []


    for empleo in empleos:
        embedding_empleo = np.array(json.loads(empleo.embeddings)).flatten()
        similitud = calcular_similitud(embedding_aspirante, embedding_empleo)
        resultados.append((empleo, similitud))

        videos_empleo = VideoPostEmpleo.objects.filter(empleo=empleo.id)
        if videos_empleo:
            for video in videos_empleo:
                resultados_video_post.append((video, similitud))


    for empresa in empresas:
        embedding_empresa = np.array(json.loads(empresa.embeddings)).flatten()
        similitud = calcular_similitud(embedding_aspirante, embedding_empresa)
        resultados_empresas.append((empresa, similitud))

    for grupo in grupos:
        embedding_grupo = np.array(json.loads(grupo.embeddings)).flatten()
        similitud = calcular_similitud(embedding_aspirante, embedding_grupo)
        resultados_grupos.append((grupo, similitud))

    resultados_grupos.sort(key=lambda x: x[1], reverse=True)
    resultados_grupos_ord = resultados_grupos[:12]
    grouped_grupos = [resultados_grupos_ord[i:i+3] for i in range(0, len(resultados_grupos_ord), 3)]


    resultados_empresas.sort(key=lambda x: x[1], reverse=True)
    resultadoFemp = resultados_empresas[:50]


    resultados.sort(key=lambda x: x[1], reverse=True)
    resultadoF = resultados[:9]
    grouped_cards = [resultadoF[i:i+3] for i in range(0, len(resultadoF), 3)]
    resultados_video_post.sort(key=lambda x: x[1], reverse=True)
    resultados_video_post_ord = resultados_video_post[:5]


    return render(request, 'home_aspirante.html', {'aspirante': aspirante, 'grouped_cards': grouped_cards, 'resultadoFemp': resultadoFemp, 'grouped_grupos': grouped_grupos, 'resultados_video_post_ord': resultados_video_post_ord})


@login_required
def home_empresa(request):
    user = request.user
    empresa = Reclutador_empresa.objects.get(usuario=user)
    embedding_empresa = np.array(json.loads(empresa.embeddings)).flatten()
    aspirantes = Aspirante.objects.all()
    grupos = GrupoInteres.objects.all()
    video_posts = Video_post.objects.all()
    resultados_aspirante = []
    resultados_grupos = []
    resultados_video_post = []

    for video_post in video_posts:
        embedding_video_post = np.array(json.loads(video_post.embeddings)).flatten()
        similitud = calcular_similitud(embedding_empresa, embedding_video_post)
        resultados_video_post.append((video_post, similitud))

    for grupo in grupos:
        embedding_grupo = np.array(json.loads(grupo.embeddings)).flatten()
        similitud = calcular_similitud(embedding_empresa, embedding_grupo)
        resultados_grupos.append((grupo, similitud))


    for aspirante in aspirantes:
        embedding_aspirante = np.array(json.loads(aspirante.embeddings)).flatten()
        similitud = calcular_similitud(embedding_empresa, embedding_aspirante)
        resultados_aspirante.append((aspirante, similitud))


    resultados_grupos.sort(key=lambda x: x[1], reverse=True)
    resultados_grupos_ord = resultados_grupos[:12]
    grouped_grupos = [resultados_grupos_ord[i:i + 3] for i in range(0, len(resultados_grupos_ord), 3)]



    resultados_aspirante.sort(key=lambda x: x[1], reverse=True)
    aspirantes = resultados_aspirante[:10]

    resultados_video_post.sort(key=lambda x: x[1], reverse=True)
    videos = resultados_video_post[:5]

    return render(request, 'home_empresa.html', {'empresa': empresa, 'grouped_grupos': grouped_grupos, 'aspirantes': aspirantes, 'videos': videos})


def calcular_similitud(embedding_aspirante, embedding_empleo):
    """Calcula la similitud coseno entre dos embeddings."""
    dot_product = np.dot(embedding_aspirante, embedding_empleo)
    norm_aspirante = np.linalg.norm(embedding_aspirante)
    norm_empleo = np.linalg.norm(embedding_empleo)
    return dot_product / (norm_aspirante * norm_empleo)






def landing(request):
    return render(request, 'landing.html')


@login_required
def editar_perfil_aspirante(request):
    user = request.user  # Assuming the user is logged in
    aspirante_instance = Aspirante.objects.get(usuario=user)
    redes_sociales_instance = aspirante_instance.redes_sociales
    idiomas_actuales = IdiomaAspirante.objects.filter(aspirante=aspirante_instance).values_list('idioma', flat=True)

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        aspirante_form = AspiranteCreationForm(request.POST, request.FILES, instance=aspirante_instance)
        redes_sociales_form = RedesSocialesForm(request.POST, instance=redes_sociales_instance)
        idioma_form = IdiomaAspiranteForm(request.POST)

        if user_form.is_valid() and aspirante_form.is_valid() and redes_sociales_form.is_valid() and idioma_form.is_valid():
            user_form.save()
            aspirante_form.save()
            redes_sociales_form.save()

            nuevos_idiomas = idioma_form.cleaned_data['idiomas']
            IdiomaAspirante.objects.filter(aspirante=aspirante_instance).exclude(idioma__in=nuevos_idiomas).delete()
            for idioma in nuevos_idiomas:
                if not IdiomaAspirante.objects.filter(aspirante=aspirante_instance, idioma=idioma).exists():
                    IdiomaAspirante.objects.create(aspirante=aspirante_instance, idioma=idioma)

            return redirect('mi_perfil')  # Redirect to the same page after saving

    else:
        user_form = CustomUserCreationForm(instance=user)
        aspirante_form = AspiranteCreationForm(instance=aspirante_instance)
        redes_sociales_form = RedesSocialesForm(instance=redes_sociales_instance)
        idioma_form = IdiomaAspiranteForm(initial={'idiomas': list(idiomas_actuales)})  # Cargar los idiomas actuales


    return render(request, 'editar_perfil_aspirante.html', {
        'user_form': user_form,
        'aspirante_form': aspirante_form,
        'redes_sociales_form': redes_sociales_form,
        'idioma_form': idioma_form
    })


@login_required
def editar_empresa(request):
    user = request.user
    empresa_instance = Reclutador_empresa.objects.get(usuario=user)
    if request.method == 'POST':
        empresa_form = ReclutadorCreationForm(request.POST, request.FILES, instance=empresa_instance)
        if empresa_form.is_valid():
            empresa_form.save()
            return redirect('mi_perfil_reclutador')
    else:
        empresa_form = ReclutadorCreationForm(instance=empresa_instance)

    return render(request, 'editar_empresa.html', {'empresa_form': empresa_form})


@login_required
def editar_reclutador(request):
    user = request.user
    if request.method == 'POST':
        user_form = CustomUserForm_sin_contra(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('mi_perfil_reclutador')
    else:
        user_form = CustomUserForm_sin_contra(instance=user)

    return render(request, 'editar_reclutador.html', {'user_form': user_form})


@login_required
def editar_aspirante_user(request):
    user = request.user
    if request.method == 'POST':
        user_form = CustomUserForm_sin_contra(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('mi_perfil_aspirante')
    else:
        user_form = CustomUserForm_sin_contra(instance=user)
    return render(request, 'editar_aspirante_user.html', {'user_form': user_form})



@login_required
def editar_representante_legal(request):
    user = request.user  # Assuming the user is logged in
    reclutador_instance = Reclutador_empresa.objects.get(usuario=user)
    representante_legal_instance = reclutador_instance.representante_legal

    if request.method == 'POST':
        representante_legal_form = RepresentanteLegalForm(request.POST, instance=representante_legal_instance)
        if representante_legal_form.is_valid():
            representante_legal_form.save()
            return redirect('mi_perfil_reclutador')  # Redirect to the same page after saving
    else:
        representante_legal_form = RepresentanteLegalForm(instance=representante_legal_instance)

    return render(request, 'editar_representante_legal.html', {
        'representante_legal_form': representante_legal_form,
    })


@login_required
def mi_perfil_reclutador(request):
    reclutador_empresa = Reclutador_empresa.objects.get(usuario=request.user)

    return render(request, 'mi_perfil_reclutador.html', {'reclutador_empresa': reclutador_empresa})


@login_required
def mi_perfil_aspirante(request):
    aspirante = Aspirante.objects.get(usuario=request.user)
    idiomas = IdiomaAspirante.objects.filter(aspirante=aspirante)
    formaciones = FormacionAspirante.objects.filter(aspirante=aspirante).order_by('fecha_inicio')
    experiencias = ExperienciaLaboral.objects.filter(aspirante=aspirante).order_by('fecha_inicio')

    return render(request, 'mi_perfil_aspirante.html', {'aspirante': aspirante, 'idiomas': idiomas, 'formaciones': formaciones, 'experiencias': experiencias})


@login_required
def change_password(request):
    base_template = 'base_aspirante.html' if hasattr(request.user, 'aspirante') else 'base_reclutador.html'

    # Crear el formulario de cambio de contraseña
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente')
            return redirect('mi_perfil_reclutador' if user.tipo_usuario == 'reclutador' else 'mi_perfil_aspirante')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'cambiar_contrasena.html', {'form': form, 'base_template': base_template})

@login_required
def editar_aspirante_aspirante(request):
    user = request.user
    aspirante_instancia = Aspirante.objects.get(usuario=user)
    if request.method == 'POST':
        aspirante_form = AspiranteCreationForm(request.POST, request.FILES, instance=aspirante_instancia)
        if aspirante_form.is_valid():
            aspirante_form.save()
            return redirect('mi_perfil_aspirante')
    else:
        aspirante_form = ReclutadorCreationForm(instance=aspirante_instancia)

    return render(request, 'editar_aspirante_aspirante.html', {'aspirante_form': aspirante_form})


@login_required
def agregar_formacion(request):
    if request.method == 'POST':
        form = FormacionAspiranteForm(request.POST)
        if form.is_valid():
            nueva_formacion = form.save(commit=False)
            nueva_formacion.aspirante = request.user.aspirante  # Asocia la formación con el aspirante actual
            nueva_formacion.save()
            return redirect('mi_perfil_aspirante')  # Redirige al perfil después de añadir la formación
    else:
        form = FormacionAspiranteForm()

    return render(request, 'agregar_formacion.html', {'form': form})


def agregar_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaLaboralForm(request.POST)
        if form.is_valid():
            nueva_experiencia = form.save(commit=False)
            nueva_experiencia.aspirante = request.user.aspirante  # Asocia la experiencia al aspirante
            nueva_experiencia.save()
            if 'añadir mas' in request.POST:
                return redirect('agregar_experiencia')

            return redirect('mi_perfil_aspirante')
    else:
        form = ExperienciaLaboralForm()

    return render(request, 'agregar_experiencia.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')
