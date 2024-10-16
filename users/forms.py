from django import forms
from .models import User, Aspirante, Reclutador_empresa, RepresentanteLegal, IdiomaAspirante, FormacionAspirante, RedesSociales, Idiomas, ExperienciaLaboral
from django.contrib.auth.forms import UserCreationForm


class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ['facebook', 'linkedin', 'twitter', 'instagram', 'github', 'youtube']
        widgets = {
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control'}),
        }


class RepresentanteLegalForm(forms.ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = ['nombre', 'documento_identidad', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nombre', 'email', 'documento_identidad', 'indicativo_pais', 'telefono', 'pais', 'ciudad', 'foto_perfil', 'tipo_usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select'}),
        }


class AspiranteCreationForm(forms.ModelForm):
    redes_sociales = RedesSocialesForm()

    class Meta:
        model = Aspirante
        fields = ['hoja_vida', 'descripcion', 'objetivos', 'sector_laboral', 'gustos_intereses', 'salario', 'modalidad_trabajo', 'disponibilidad_de_empezar', 'disponibilidad_viajar', 'proyectos', 'competencias_tecnicas', 'habilidades_blandas','palabras_clave', 'idioma_natal', 'video_presentacion']
        widgets = {
            'sector_laboral': forms.Select(attrs={'class': 'form-control'}),
            'hoja_vida': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'modalidad_trabajo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'objetivos': forms.Textarea(attrs={'class': 'form-control'}),
            'gustos_intereses': forms.Textarea(attrs={'class': 'form-control'}),
            'proyectos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video_presentacion': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'disponibilidad_de_empezar': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'competencias_tecnicas': forms.Textarea(attrs={'class': 'form-control'}),
            'habilidades_blandas': forms.Textarea(attrs={'class': 'form-control'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control'}),

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

            'mision': forms.Textarea(attrs={'class': 'form-control'}),
            'vision': forms.Textarea(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'palabras_clave': forms.Textarea(attrs={'class': 'form-control'}),
            'registro_camara_comercio': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class ExperienciaLaboralForm(forms.ModelForm):
    class Meta:
        model = ExperienciaLaboral
        fields = ['titulo_puesto', 'empresa', 'fecha_inicio', 'fecha_fin', 'descripcion']

        widgets = {
            'titulo_puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserForm_sin_contra(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nombre', 'email', 'documento_identidad', 'indicativo_pais', 'telefono', 'pais', 'ciudad', 'foto_perfil', 'tipo_usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select'}),
        }
