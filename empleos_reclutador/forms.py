from django import forms
from .models import Empleo, VideoPostEmpleo


class EmpleoForm(forms.ModelForm):
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
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'habilidades': forms.Textarea(attrs={'class': 'form-control'}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control'}),
            'nivel_estudios': forms.Textarea(attrs={'class': 'form-control'}),
            'modalidad_trabajo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control'}),
            'competencias_tecnicas': forms.Textarea(attrs={'class': 'form-control'}),
            'video_presentacion': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }


class VideoPostEmpleo_form(forms.ModelForm):
    class Meta:
        model = VideoPostEmpleo
        fields = ['video_file', 'thumbnail']

        widgets = {
            'video_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'})
                }
