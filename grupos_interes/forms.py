# forms.py
from django import forms
from .models import Publicacion, Comentario, GrupoInteres
from users.models import User, Aspirante, Reclutador_empresa
from empleos_reclutador.models import Empleo


class GrupoInteresForm(forms.ModelForm):
    class Meta:
        model = GrupoInteres
        fields = ['nombre', 'descripcion', 'image']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class PublicacionForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=Publicacion.TIPO_PUBLICACION,
        widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle', 'id': 'tipo'})
    )

    reclutador_empresa = forms.ModelChoiceField(
        queryset=Reclutador_empresa.objects.all(),
        label="reclutador empresa",
        widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle'})
    )

    aspirante = forms.ModelChoiceField(
        queryset=Aspirante.objects.all(),
        label="aspirante",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle'})
    )

    empleo = forms.ModelChoiceField(
        queryset=Empleo.objects.all(),
        label="empleo",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle'})
    )

    class Meta:
        model = Publicacion
        fields = ['tipo', 'contenido', 'recurso', 'reclutador_empresa', 'aspirante', 'empleo']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'placeholder': 'Escribe tu pregunta, consejo o recomendación aquí'}),
            'recurso': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'placeholder': 'Deja tu comentario'}),
        }
