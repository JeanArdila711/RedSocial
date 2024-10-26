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
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class PublicacionForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        choices=Publicacion.TIPO_PUBLICACION,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'tipo'})
    )

    reclutador_empresa = forms.ModelChoiceField(
        queryset=Reclutador_empresa.objects.all(),
        label="reclutador empresa",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    aspirante = forms.ModelChoiceField(
        queryset=Aspirante.objects.all(),
        label="aspirante",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    empleo = forms.ModelChoiceField(
        queryset=Empleo.objects.all(),
        label="empleo",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Publicacion
        fields = ['tipo', 'contenido', 'recurso', 'reclutador_empresa', 'aspirante', 'empleo']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu pregunta, consejo o recomendación aquí'}),
            'recurso': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deja tu comentario'}),
        }
