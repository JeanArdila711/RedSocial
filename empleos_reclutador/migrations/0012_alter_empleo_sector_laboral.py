# Generated by Django 5.1.1 on 2024-11-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos_reclutador', '0011_alter_empleo_sector_laboral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleo',
            name='sector_laboral',
            field=models.CharField(choices=[('estilismo_ciudadopersonal', 'Estilismo y cuidado personal'), ('administracion empresarial', 'Administracion Empresarial'), ('tecnologia_de_la_informacion', 'Tecnologia de la Informacion'), ('finanzas_y_contabilidad', 'Finanzas y Contabilidad'), ('salud', 'Salud'), ('educacion', 'Educacion'), ('ingenieria', 'Ingenieria'), ('marketing_y_publicidad', 'Marketing y Publicidad'), ('ventas', 'Ventas'), ('servicios_al_cliente', 'Servicios al Cliente'), ('construccion', 'Construccion'), ('manufactura', 'Manufactura'), ('recursos_humanos', 'Recursos Humanos'), ('artes_y_entretenimiento', 'Artes y Entretenimiento'), ('turismo_y_hospitalidad', 'Turismo y Hospitalidad'), ('transporte_y_logistica', 'Transporte y Logistica'), ('legal', 'Legal'), ('investigacion_y_desarrollo', 'Investigacion y Desarrollo'), ('energia_y_recursos_naturales', 'Energia y Recursos Naturales'), ('servicios_profesionales', 'Servicios Profesionales'), ('medios_de_comunicacion', 'Medios de Comunicacion'), ('agricultura', 'Agricultura'), ('gobierno_y_administracion_publica', 'Gobierno y Administracion Publica'), ('ciencia_y_tecnologia', 'Ciencia y Tecnologia'), ('servicios_sociales', 'Servicios Sociales'), ('medio_ambiente', 'Medio Ambiente'), ('comercio_y_retail', 'Comercio y Retail')], max_length=50),
        ),
    ]
