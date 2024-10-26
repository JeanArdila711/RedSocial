# Generated by Django 5.1.1 on 2024-10-25 14:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleos_reclutador', '0007_empleo_embeddings'),
        ('users', '0016_reclutador_empresa_palabras_clave'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoInteres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('verificado', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('miembros', models.ManyToManyField(related_name='grupos_interes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('pregunta', 'Pregunta'), ('consejo', 'Consejo'), ('recomendacion', 'Recomendación')], max_length=20)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('recurso', models.FileField(blank=True, null=True, upload_to='grupos_recursos/')),
                ('aspirante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.aspirante')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('empleo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleos_reclutador.empleo')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicaciones', to='grupos_interes.grupointeres')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_publicacion', to=settings.AUTH_USER_MODEL)),
                ('reclutador_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.reclutador_empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='grupos_interes.publicacion')),
            ],
        ),
    ]
