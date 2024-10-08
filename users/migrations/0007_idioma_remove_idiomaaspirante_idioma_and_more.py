# Generated by Django 5.1.1 on 2024-09-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_foto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('ingles', 'ingles'), ('espanol', 'espanol'), ('chino', 'chino'), ('frances', 'frances'), ('aleman', 'aleman'), ('portugues', 'portugues'), ('italiano', 'italiano'), ('arabe', 'arabe'), ('japones', 'japones'), ('ruso', 'ruso'), ('holandes', 'holandes'), ('coreano', 'coreano'), ('sueco', 'sueco'), ('turco', 'turco'), ('hindi', 'hindi'), ('hebreo', 'hebreo'), ('polaco', 'polaco'), ('griego', 'griego'), ('checo', 'checo'), ('danes', 'danes')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='idiomaaspirante',
            name='idioma',
        ),
        migrations.AddField(
            model_name='idiomaaspirante',
            name='idiomas',
            field=models.ManyToManyField(related_name='aspirantes', to='users.idioma'),
        ),
    ]
