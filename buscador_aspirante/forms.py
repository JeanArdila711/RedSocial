from django import forms
from .models import Video_post


class CrearVideoForm(forms.ModelForm):
    class Meta:
        model = Video_post
        fields = [
            'titulo', 'descripcion', 'video_post', 'palabras_clave'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'video_post': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
        }
