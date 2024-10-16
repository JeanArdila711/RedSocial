# generar_embeddings_empleos.py
from django.core.management.base import BaseCommand
from empleos_reclutador.models import Empleo

class Command(BaseCommand):
    help = 'Genera embeddings para todos los Empleos existentes en la base de datos'

    def handle(self, *args, **kwargs):
        empleos = Empleo.objects.all()
        for empleo in empleos:
            try:
                # Llama al método set_embeddings() para cada aspirante
                empleo.set_embeddings()
                self.stdout.write(self.style.SUCCESS(f'Embeddings generados para {empleo.titulo[:30]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error al generar embeddings para {empleo.titulo[:30]}...: {e}'))

        self.stdout.write(self.style.SUCCESS('Embeddings generados para todos los empleos.'))
