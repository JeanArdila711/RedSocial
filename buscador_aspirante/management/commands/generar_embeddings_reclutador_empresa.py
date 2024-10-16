# generate_embeddings.py
from django.core.management.base import BaseCommand
from users.models import Reclutador_empresa

class Command(BaseCommand):
    help = 'Genera embeddings para todos los reclutadores existentes en la base de datos'

    def handle(self, *args, **kwargs):
        reclutador_empresa = Reclutador_empresa.objects.all()
        for reclutador in reclutador_empresa:
            try:
                # Llama al método set_embeddings() para cada aspirante
                reclutador.set_embeddings()
                self.stdout.write(self.style.SUCCESS(f'Embeddings generados para {reclutador.nombre_empresa}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al generar embeddings para {reclutador.nombre_empresa}: {e}'))

        self.stdout.write(self.style.SUCCESS('Embeddings generados para todos los reclutadores.'))
