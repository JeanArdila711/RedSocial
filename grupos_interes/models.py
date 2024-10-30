from django.db import models
from django.utils import timezone
from users.models import User, Reclutador_empresa, Aspirante
from empleos_reclutador.models import Empleo
import json
import numpy as np
import openai
from django.conf import settings


class GrupoInteres(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, related_name="grupos_interes", blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='image_grupo_interes/', default='image_grupo_interes/def.png', null=True, blank=True)
    activo = models.BooleanField(default=True)
    embeddings = models.TextField(blank=True, null=True)

    def set_embeddings(self):
        """Genera y almacena el embedding para el video post."""
        texto_completo = (
            f"Nombre del grupo: {self.nombre}"
            f"Descripcion: {self.descripcion} "
        )

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
        return self.nombre


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.autor} comentó en {self.publicacion.id}"

class Publicacion(models.Model):
    TIPO_PUBLICACION = [
        ('pregunta', 'Pregunta'),
        ('consejo', 'Consejo'),
        ('recomendacion', 'Recomendación'),
    ]
    grupo = models.ForeignKey(GrupoInteres, on_delete=models.CASCADE, related_name='publicaciones')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_PUBLICACION)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    recurso = models.FileField(upload_to='grupos_recursos/', null=True, blank=True)

    reclutador_empresa = models.ForeignKey(Reclutador_empresa, null=True, blank=True, on_delete=models.SET_NULL)
    aspirante = models.ForeignKey(Aspirante, null=True, blank=True, on_delete=models.SET_NULL)
    empleo = models.ForeignKey(Empleo, null=True, blank=True, on_delete=models.SET_NULL)
    comentarios = models.ManyToManyField(Comentario, related_name="grupos_interes", blank=True)
    likes = models.ManyToManyField(User, related_name='likes_publicacion', blank=True)

    def __str__(self):
        return f"{self.autor} - {self.tipo} - {self.grupo.nombre}"

