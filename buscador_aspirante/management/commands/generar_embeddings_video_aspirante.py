# generate_embeddings.py
from django.core.management.base import BaseCommand
from buscador_aspirante.models import Video_post

class Command(BaseCommand):
    help = 'Genera embeddings para todos los videoPost de aspirantes existentes en la base de datos'

    def handle(self, *args, **kwargs):
        video_posts = Video_post.objects.all()
        for video_post in video_posts:
            try:
                # Llama al método set_embeddings() para cada aspirante
                video_post.set_embeddings()
                self.stdout.write(self.style.SUCCESS(f'Embeddings generados para {video_post.titulo}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al generar embeddings para {video_post.titulo}: {e}'))

        self.stdout.write(self.style.SUCCESS('Embeddings generados para todos los aspirantes.'))
