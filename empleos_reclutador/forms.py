from django import forms
from .models import Empleo


class EmpleoForm(forms.ModelForm):
    palabras_clave = forms.CharField(required=False, help_text="Ingresa palabras clave separadas por comas.")
    class Meta:
        model = Empleo
        fields = [
            'titulo', 'sector_laboral', 'salario', 'pais', 'ciudad',
            'descripcion', 'habilidades', 'experiencia', 'nivel_estudios', 'modalidad_trabajo',
            'palabras_clave', 'tipo_contrato', 'competencias_tecnicas', 'video_presentacion'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sector_laboral': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 5}),
            'habilidades': forms.Textarea(attrs={'rows': 3}),
            'experiencia': forms.Textarea(attrs={'rows': 3}),
            'nivel_estudios': forms.Textarea(attrs={'rows': 3}),
            'modalidad_trabajo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
            'competencias_tecnicas': forms.Textarea(attrs={'rows': 3}),
            'video_presentacion': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }

