# Generated by Django 5.1.1 on 2024-09-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_reclutador_reclutador_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='profile_photos/default_profile.png', null=True, upload_to='profile_photos/'),
        ),
    ]
