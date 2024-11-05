from django import forms
from .models import Empleo, VideoPostEmpleo, Oferta
from users.models import Aspirante



class EmpleoForm(forms.ModelForm):
    class Meta:
        model = Empleo
        fields = [
            'titulo', 'sector_laboral', 'salario', 'pais', 'ciudad',
            'descripcion', 'habilidades', 'experiencia', 'nivel_estudios', 'modalidad_trabajo',
            'palabras_clave', 'tipo_contrato', 'competencias_tecnicas', 'habilidades_blandas', 'video_presentacion'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-body-tertiary bg-dark-subtle'}),
            'sector_laboral': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'pais': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'habilidades': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'experiencia': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'nivel_estudios': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'modalidad_trabajo': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 2}),
            'habilidades_blandas': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'competencias_tecnicas': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle', 'rows': 3}),
            'video_presentacion': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class VideoPostEmpleo_form(forms.ModelForm):
    class Meta:
        model = VideoPostEmpleo
        fields = ['video_file', 'thumbnail']

        widgets = {
            'video_file': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'})
                }


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['mensaje', 'empleo']

        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control shadow', 'rows': 3}),
        }

    def __init__(self, reclutador, *args, **kwargs):
        super(OfertaForm, self).__init__(*args, **kwargs)

        # Filtrar empleos según el reclutador proporcionado
        self.fields['empleo'] = forms.ModelChoiceField(
            queryset=Empleo.objects.filter(reclutador=reclutador),
            label="Empleos",
            widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle'})  # Clase Bootstrap
        )
