# Generated by Django 5.1.1 on 2024-09-27 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reclutador',
            new_name='Reclutador_empresa',
        ),
    ]
