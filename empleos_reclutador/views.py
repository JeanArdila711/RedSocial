from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleoForm
from .models import Empleo
from users.models import Reclutador_empresa, Aspirante




def crear_empleo(request):
    if request.method == 'POST':
        form = EmpleoForm(request.POST, request.FILES)
        if form.is_valid():
            empleo = form.save(commit=False)
            empleo.reclutador = request.user.reclutador_empresa  # Asigna el reclutador actual
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
    return render(request, 'detalle_empleo.html', {'empleo': empleo})


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
