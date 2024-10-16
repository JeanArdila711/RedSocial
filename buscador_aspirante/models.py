from django.db import models
from users.models import Aspirante
from empleos_reclutador.models import Empleo
from django.utils import timezone
from django.conf import settings
import openai
import json
import numpy as np


class Postulacion(models.Model):
    aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)


class Favoritos(models.Model):
    aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)


class Video_post(models.Model):
    aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    video_post = models.FileField(upload_to='videos_post_aspirante/')
    palabras_clave = models.TextField()
    embeddings = models.TextField(blank=True, null=True)

    def set_embeddings(self):
        """Genera y almacena el embedding para el video post."""
        texto_completo = (
            f"{self.descripcion} "
            f"{self.palabras_clave}"
        )

        embedding_aspirante = np.array(
            json.loads(self.aspirante.embeddings)) if self.aspirante.embeddings else np.zeros(1536)

        openai.api_key = settings.OPENAI_API_KEY

        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = np.array(response.data[0].embedding)

            # Promediar los embeddings
            combined_embedding = (embedding_data + embedding_aspirante) / 2

            self.embeddings = json.dumps(combined_embedding.tolist())
            self.save()
        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')

    def __str__(self):
        return self.titulo