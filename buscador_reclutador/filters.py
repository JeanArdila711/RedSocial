# filters.py
import django_filters
from django_filters import DateFilter, ChoiceFilter
from users.models import Aspirante
from djmoney.forms.fields import MoneyField

class AspiranteFilter(django_filters.FilterSet):
    # Filtros básicos
    sector_laboral = django_filters.ChoiceFilter(choices=Aspirante.SectoresLaborales.choices, label="Sector Laboral")
    modalidad_trabajo = ChoiceFilter(choices=Aspirante.MODALIDAD_TRABAJO, label="Modalidad de Trabajo")
    salario__gte = django_filters.NumberFilter(field_name='salario', lookup_expr='gte', label="Salario mínimo")
    salario__lte = django_filters.NumberFilter(field_name='salario', lookup_expr='lte', label="Salario máximo")
    disponibilidad_de_empezar = DateFilter(field_name="disponibilidad_de_empezar", lookup_expr='gte', label="Disponible a partir de")

    class Meta:
        model = Aspirante
        fields = [
            'sector_laboral',
            'modalidad_trabajo',
            'salario',
            'disponibilidad_de_empezar',
            'disponibilidad_viajar',
            'idioma_natal'
        ]
