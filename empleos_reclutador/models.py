from django.db import models
from users.models import Reclutador_empresa, SectoresLaborales, Paises
from djmoney.models.fields import MoneyField
from django.utils import timezone
import openai
import json
from decouple import config
from django.conf import settings


# Create your models here.
class Empleo(models.Model):
    reclutador = models.ForeignKey(Reclutador_empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    sector_laboral = models.CharField(max_length=50, choices=SectoresLaborales.choices)
    salario = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='COP',  # Moneda predeterminada para Colombia
        currency_choices=[
            ('COP', 'Peso colombiano (COP)'),  # Empleos locales
            ('USD', 'Dólar estadounidense (USD)'),  # Empleos virtuales (EE.UU.)
            ('EUR', 'Euro (EUR)'),  # Empleos virtuales (Europa)
            ('GBP', 'Libra esterlina (GBP)'),  # Empleos virtuales (Reino Unido)
            ('CAD', 'Dólar canadiense (CAD)'),  # Empleos virtuales (Canadá)
            ('AUD', 'Dólar australiano (AUD)'),  # Empleos virtuales (Australia)
            ('BTC', 'Bitcoin (BTC)'),  # Criptomonedas
            ('ETH', 'Ethereum (ETH)'),  # Criptomonedas
        ]
    )
    pais = models.CharField(max_length=50, choices=Paises.choices)
    ciudad = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Campo de fecha y hora
    descripcion = models.TextField()
    habilidades = models.TextField()
    experiencia = models.TextField()
    nivel_estudios = models.TextField()
    MODALIDAD_TRABAJO = [('virtual', 'virtual'), ('presencial', 'presencial'), ('mixto', 'mixto')]
    modalidad_trabajo = models.CharField(max_length=50, choices=MODALIDAD_TRABAJO)
    palabras_clave = models.TextField()

    CONTRATO_CHOICES = [
        ('termino_fijo', 'Contrato a Término Fijo'),
        ('termino_indefinido', 'Contrato a Término Indefinido'),
        ('aprendizaje', 'Contrato de Aprendizaje'),
        ('obra_labor', 'Contrato por Obra o Labor'),
        ('tiempo_parcial', 'Contrato a Tiempo Parcial'),
        ('teletrabajo', 'Contrato de Teletrabajo'),
        ('temporada', 'Contrato de Temporada'),
        ('servicios', 'Contrato de Servicios'),
    ]
    tipo_contrato = models.CharField(
        max_length=30,
        choices=CONTRATO_CHOICES,
        default='termino_fijo'  # Puedes cambiar el valor por defecto
    )
    competencias_tecnicas = models.TextField()
    habilidades_blandas = models.TextField(blank=True, null=True)

    video_presentacion = models.FileField(upload_to='videos_presentacion_empleo/')
    embeddings = models.TextField(blank=True, null=True)  # Para almacenar embeddings en formato JSON

    def set_embeddings(self):
        """Genera y almacena el embedding para el empleo."""

        texto_completo = f"{self.descripcion} {self.habilidades} {self.experiencia} {self.nivel_estudios} {self.palabras_clave}"

        openai.api_key = settings.OPENAI_API_KEY

        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = response.data[0].embedding
            self.embeddings = json.dumps(embedding_data)  # Almacenar como un único embedding
            self.save()
        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')

    def __str__(self):
        return self.titulo


class VideoPostEmpleo(models.Model):
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE, related_name='videos_empleo')
    video_file = models.FileField(upload_to='post_video_empleo/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)


class Like(models.Model):
    Empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    VideoPostEmpleo = models.ForeignKey(VideoPostEmpleo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Empleo', 'VideoPostEmpleo')
