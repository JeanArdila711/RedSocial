# generate_embeddings.py
from django.core.management.base import BaseCommand
from users.models import Aspirante

class Command(BaseCommand):
    help = 'Genera embeddings para todos los aspirantes existentes en la base de datos'

    def handle(self, *args, **kwargs):
        aspirantes = Aspirante.objects.all()
        for aspirante in aspirantes:
            try:
                # Llama al método set_embeddings() para cada aspirante
                aspirante.set_embeddings()
                self.stdout.write(self.style.SUCCESS(f'Embeddings generados para {aspirante.usuario.nombre}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al generar embeddings para {aspirante.usuario.nombre}: {e}'))

        self.stdout.write(self.style.SUCCESS('Embeddings generados para todos los aspirantes.'))
