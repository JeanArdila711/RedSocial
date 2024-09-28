# Generated by Django 5.1.1 on 2024-09-28 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos_reclutador', '0001_initial'),
        ('users', '0005_rename_reclutador_reclutador_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleo',
            name='palabras_clave',
        ),
        migrations.AlterField(
            model_name='empleo',
            name='reclutador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.reclutador_empresa'),
        ),
        migrations.DeleteModel(
            name='PalabraClave',
        ),
        migrations.AddField(
            model_name='empleo',
            name='palabras_clave',
            field=models.TextField(blank=True, null=True),
        ),
    ]
