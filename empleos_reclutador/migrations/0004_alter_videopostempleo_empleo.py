# Generated by Django 5.1.1 on 2024-09-30 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos_reclutador', '0003_videopostempleo_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopostempleo',
            name='empleo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos_empleo', to='empleos_reclutador.empleo'),
        ),
    ]
