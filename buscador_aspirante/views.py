from django.shortcuts import render, get_object_or_404
from empleos_reclutador.models import Empleo
# Create your views here.


def empleos_aspirante(request):
    empleos = Empleo.objects.all()
    return render(request, 'empleos_aspirante.html', {'empleos': empleos})


def detalle_empleo_aspirante(request, empleo_id):
    empleo = get_object_or_404(Empleo, id=empleo_id)
    return render(request, 'detalle_empleo_aspirante.html', {'empleo': empleo})

