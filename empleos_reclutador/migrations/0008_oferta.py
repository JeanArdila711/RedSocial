# Generated by Django 5.1.1 on 2024-11-03 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos_reclutador', '0007_empleo_embeddings'),
        ('users', '0016_reclutador_empresa_palabras_clave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.aspirante')),
                ('reclutador_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.reclutador_empresa')),
            ],
        ),
    ]
