from django import forms
from .models import User, Aspirante, Reclutador_empresa, RepresentanteLegal, IdiomaAspirante, FormacionAspirante, RedesSociales, Idiomas, ExperienciaLaboral
from django.contrib.auth.forms import UserCreationForm


class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ['facebook', 'linkedin', 'twitter', 'instagram', 'github', 'youtube']
        widgets = {
            'facebook': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'github': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class RepresentanteLegalForm(forms.ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = ['nombre', 'documento_identidad', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'email', 'documento_identidad', 'indicativo_pais', 'telefono', 'pais', 'ciudad', 'foto_perfil']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'pais': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class AspiranteCreationForm(forms.ModelForm):
    redes_sociales = RedesSocialesForm()

    class Meta:
        model = Aspirante
        fields = ['hoja_vida', 'descripcion', 'objetivos', 'sector_laboral', 'gustos_intereses', 'salario', 'modalidad_trabajo', 'disponibilidad_de_empezar', 'disponibilidad_viajar', 'proyectos', 'competencias_tecnicas', 'habilidades_blandas','palabras_clave', 'idioma_natal', 'video_presentacion']
        widgets = {
            'sector_laboral': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'hoja_vida': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'modalidad_trabajo': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'objetivos': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'gustos_intereses': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'proyectos': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'video_presentacion': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'disponibilidad_de_empezar': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark-subtle'}),
            'competencias_tecnicas': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'habilidades_blandas': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),

        }
    def save(self, commit=True):
        aspirante = super().save(commit=False)
        if commit:
            aspirante.save()
        return aspirante


class ReclutadorCreationForm(forms.ModelForm):
    class Meta:
        model = Reclutador_empresa
        fields = ['nombre_empresa', 'NIT', 'mision', 'vision', 'cantidad_empleados', 'sede_principal', 'registro_camara_comercio', 'logo', 'descripcion', 'palabras_clave']
        widgets = {

            'mision': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'vision': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control bg-dark-subtle'}),
            'registro_camara_comercio': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class IdiomaAspiranteForm(forms.Form):  # Cambiamos a forms.Form en vez de forms.ModelForm
    idiomas = forms.MultipleChoiceField(
        choices=Idiomas.choices,  # Usamos las choices del TextChoices
        widget=forms.CheckboxSelectMultiple,  # O puedes usar SelectMultiple si prefieres dropdown
        label="Selecciona tus idiomas"
    )


class FormacionAspiranteForm(forms.ModelForm):
    class Meta:
        model = FormacionAspirante
        fields = ['titulo', 'institucion', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark-subtle'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark-subtle'}),
        }


class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = ['titulo_puesto', 'empresa', 'fecha_inicio', 'fecha_fin', 'descripcion']

        widgets = {
            'titulo_puesto': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark-subtle'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-dark-subtle'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
        }


class CustomUserForm_sin_contra(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nombre', 'email', 'documento_identidad', 'indicativo_pais', 'telefono', 'pais', 'ciudad', 'foto_perfil', 'tipo_usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'pais': forms.Select(attrs={'class': 'form-control bg-dark-subtle'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control bg-dark-subtle'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select bg-dark-subtle'}),
        }
