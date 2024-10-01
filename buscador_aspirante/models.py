from django.db import models
from users.models import Aspirante
from empleos_reclutador.models import Empleo
from django.utils import timezone


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



