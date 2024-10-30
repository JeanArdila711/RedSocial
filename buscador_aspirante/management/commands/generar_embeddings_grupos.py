# generar_embeddings_empleos.py
from django.core.management.base import BaseCommand
from grupos_interes.models import GrupoInteres

class Command(BaseCommand):
    help = 'Genera embeddings para todos los Empleos existentes en la base de datos'

    def handle(self, *args, **kwargs):
        grupos = GrupoInteres.objects.all()
        for grupo in grupos:
            try:
                # Llama al método set_embeddings() para cada aspirante
                grupo.set_embeddings()
                self.stdout.write(self.style.SUCCESS(f'Embeddings generados para {grupo.nombre[:30]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al generar embeddings para {grupo.nombre[:30]}...: {e}'))

        self.stdout.write(self.style.SUCCESS('Embeddings generados para todos los empleos.'))
