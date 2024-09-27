from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, AspiranteCreationForm, ReclutadorCreationForm, RepresentanteLegalForm, IdiomaAspiranteForm, FormacionAspiranteForm, RedesSocialesForm
from .models import Aspirante
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def registrar_aspirante(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES)
        aspirante_form = AspiranteCreationForm(request.POST, request.FILES)
        redes_sociales_form = RedesSocialesForm(request.POST, request.FILES, prefix='redes_sociales')


        if user_form.is_valid() and aspirante_form.is_valid():
            user = user_form.save()
            aspirante = aspirante_form.save(commit=False)
            redes_sociales = redes_sociales_form.save()
            aspirante.usuario = user
            aspirante.redes_sociales = redes_sociales
            aspirante.save()

            login(request, user)  # Auto-login after registration
            return redirect('completar_detalles', aspirante_id=aspirante.id)  # Redirect to a profile or another page
    else:
        user_form = CustomUserCreationForm()
        aspirante_form = AspiranteCreationForm()
        redes_sociales_form = RedesSocialesForm(prefix='redes_sociales')


    return render(request, 'register_aspirante.html', {
        'user_form': user_form,
        'aspirante_form': aspirante_form,
        'redes_sociales_form': redes_sociales_form,  # Pasa el formulario al contexto

    })


def registrar_reclutador(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, request.FILES, prefix='user')
        reclutador_form = ReclutadorCreationForm(request.POST, request.FILES, prefix='reclutador')
        representante_legal_form = RepresentanteLegalForm(request.POST, request.FILES, prefix='representante_legal')

        if user_form.is_valid() and representante_legal_form.is_valid() and reclutador_form.is_valid():
            user = user_form.save()
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
        idioma_form = IdiomaAspiranteForm(request.POST)
        formacion_form = FormacionAspiranteForm(request.POST)

        if idioma_form.is_valid() and formacion_form.is_valid():
            idioma = idioma_form.save(commit=False)
            idioma.aspirante = aspirante
            idioma.save()

            formacion = formacion_form.save(commit=False)
            formacion.aspirante = aspirante
            formacion.save()

            return redirect('home_aspirante')  # Redirect to a profile or another page
    else:
        idioma_form = IdiomaAspiranteForm()
        formacion_form = FormacionAspiranteForm()

    return render(request, 'completar_detalles.html', {
        'idioma_form': idioma_form,
        'formacion_form': formacion_form
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Redireccionar basado en el tipo de usuario
            if user.tipo_usuario == 'Aspirante':
                return redirect('home_aspirante')
            elif user.tipo_usuario == 'Reclutador':
                return redirect('home_empresa')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def home_aspirante(request):
    return render(request, 'home_aspirante.html')


@login_required
def home_empresa(request):
    return render(request, 'home_empresa.html')


def landing(request):
    return render(request, 'landing.html')
