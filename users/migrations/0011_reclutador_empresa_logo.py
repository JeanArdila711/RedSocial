# Generated by Django 5.1.1 on 2024-09-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_foto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclutador_empresa',
            name='logo',
            field=models.ImageField(blank=True, default='logo_empresas/Logotipo_empresa.png', null=True, upload_to='logo_empresas/'),
        ),
    ]
