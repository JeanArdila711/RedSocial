# Generated by Django 5.1.1 on 2024-09-28 17:14

import django.db.models.deletion
import django.utils.timezone
import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_rename_reclutador_reclutador_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalabraClave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('sector_laboral', models.CharField(choices=[('tecnologia_de_la_informacion', 'Tecnologia de la Informacion'), ('finanzas_y_contabilidad', 'Finanzas y Contabilidad'), ('salud', 'Salud'), ('educacion', 'Educacion'), ('ingenieria', 'Ingenieria'), ('marketing_y_publicidad', 'Marketing y Publicidad'), ('ventas', 'Ventas'), ('servicios_al_cliente', 'Servicios al Cliente'), ('construccion', 'Construccion'), ('manufactura', 'Manufactura'), ('recursos_humanos', 'Recursos Humanos'), ('artes_y_entretenimiento', 'Artes y Entretenimiento'), ('turismo_y_hospitalidad', 'Turismo y Hospitalidad'), ('transporte_y_logistica', 'Transporte y Logistica'), ('legal', 'Legal'), ('investigacion_y_desarrollo', 'Investigacion y Desarrollo'), ('energia_y_recursos_naturales', 'Energia y Recursos Naturales'), ('servicios_profesionales', 'Servicios Profesionales'), ('medios_de_comunicacion', 'Medios de Comunicacion'), ('agricultura', 'Agricultura'), ('gobierno_y_administracion_publica', 'Gobierno y Administracion Publica'), ('ciencia_y_tecnologia', 'Ciencia y Tecnologia'), ('servicios_sociales', 'Servicios Sociales'), ('medio_ambiente', 'Medio Ambiente'), ('comercio_y_retail', 'Comercio y Retail')], max_length=50)),
                ('salario_currency', djmoney.models.fields.CurrencyField(choices=[('COP', 'Peso colombiano (COP)'), ('USD', 'Dólar estadounidense (USD)'), ('EUR', 'Euro (EUR)'), ('GBP', 'Libra esterlina (GBP)'), ('CAD', 'Dólar canadiense (CAD)'), ('AUD', 'Dólar australiano (AUD)'), ('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)')], default='COP', editable=False, max_length=3)),
                ('salario', djmoney.models.fields.MoneyField(currency_choices=[('COP', 'Peso colombiano (COP)'), ('USD', 'Dólar estadounidense (USD)'), ('EUR', 'Euro (EUR)'), ('GBP', 'Libra esterlina (GBP)'), ('CAD', 'Dólar canadiense (CAD)'), ('AUD', 'Dólar australiano (AUD)'), ('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)')], decimal_places=2, default_currency='COP', max_digits=14)),
                ('pais', models.CharField(choices=[('Afganistán', 'Afganistán'), ('Albania', 'Albania'), ('Alemania', 'Alemania'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua y Barbuda', 'Antigua y Barbuda'), ('Arabia Saudita', 'Arabia Saudita'), ('Argelia', 'Argelia'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaiyán', 'Azerbaiyán'), ('Bahamas', 'Bahamas'), ('Baréin', 'Baréin'), ('Bangladés', 'Bangladés'), ('Barbados', 'Barbados'), ('Belice', 'Belice'), ('Benín', 'Benín'), ('Bielorrusia', 'Bielorrusia'), ('Birmania', 'Birmania'), ('Bolivia', 'Bolivia'), ('Bosnia y Herzegovina', 'Bosnia y Herzegovina'), ('Botsuana', 'Botsuana'), ('Brasil', 'Brasil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Bután', 'Bután'), ('Cabo Verde', 'Cabo Verde'), ('Camboya', 'Camboya'), ('Camerún', 'Camerún'), ('Canadá', 'Canadá'), ('Catar', 'Catar'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Chipre', 'Chipre'), ('Colombia', 'Colombia'), ('Comoras', 'Comoras'), ('Congo (Brazzaville)', 'Congo (Brazzaville)'), ('Congo (Kinshasa)', 'Congo (Kinshasa)'), ('Costa Rica', 'Costa Rica'), ('Croacia', 'Croacia'), ('Cuba', 'Cuba'), ('Dinamarca', 'Dinamarca'), ('Dominica', 'Dominica'), ('Ecuador', 'Ecuador'), ('Egipto', 'Egipto'), ('El Salvador', 'El Salvador'), ('Guinea Ecuatorial', 'Guinea Ecuatorial'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('España', 'España'), ('Estados Unidos', 'Estados Unidos'), ('Filipinas', 'Filipinas'), ('Finlandia', 'Finlandia'), ('Fiyi', 'Fiyi'), ('Francia', 'Francia'), ('Gabón', 'Gabón'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Ghana', 'Ghana'), ('Grecia', 'Grecia'), ('Granada', 'Granada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bisáu', 'Guinea-Bisáu'), ('Guyana', 'Guyana'), ('Haití', 'Haití'), ('Honduras', 'Honduras'), ('Hungría', 'Hungría'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Irán', 'Irán'), ('Irak', 'Irak'), ('Irlanda', 'Irlanda'), ('Islandia', 'Islandia'), ('Israel', 'Israel'), ('Italia', 'Italia'), ('Jamaica', 'Jamaica'), ('Japón', 'Japón'), ('Jordania', 'Jordania'), ('Kazajistán', 'Kazajistán'), ('Kenia', 'Kenia'), ('Kirguistán', 'Kirguistán'), ('Kiribati', 'Kiribati'), ('Kosovo', 'Kosovo'), ('Letonia', 'Letonia'), ('Líbano', 'Líbano'), ('Liberia', 'Liberia'), ('Libia', 'Libia'), ('Liechtenstein', 'Liechtenstein'), ('Lituania', 'Lituania'), ('Luxemburgo', 'Luxemburgo'), ('Madagascar', 'Madagascar'), ('Malasia', 'Malasia'), ('Malawi', 'Malawi'), ('Maldivas', 'Maldivas'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marruecos', 'Marruecos'), ('Mauricio', 'Mauricio'), ('Mauritania', 'Mauritania'), ('México', 'México'), ('Micronesia', 'Micronesia'), ('Moldavia', 'Moldavia'), ('Mónaco', 'Mónaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Mozambique', 'Mozambique'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Nicaragua', 'Nicaragua'), ('Níger', 'Níger'), ('Nigeria', 'Nigeria'), ('Noruega', 'Noruega'), ('Nueva Zelanda', 'Nueva Zelanda'), ('Omán', 'Omán'), ('Pakistán', 'Pakistán'), ('Palau', 'Palau'), ('Panamá', 'Panamá'), ('Papúa Nueva Guinea', 'Papúa Nueva Guinea'), ('Paraguay', 'Paraguay'), ('Perú', 'Perú'), ('Polonia', 'Polonia'), ('Portugal', 'Portugal'), ('República Centroafricana', 'República Centroafricana'), ('República Checa', 'República Checa'), ('República del Congo', 'República del Congo'), ('Rumanía', 'Rumanía'), ('Rusia', 'Rusia'), ('Ruanda', 'Ruanda'), ('San Cristóbal y Nieves', 'San Cristóbal y Nieves'), ('Santa Lucía', 'Santa Lucía'), ('San Marino', 'San Marino'), ('Santo Tomé y Príncipe', 'Santo Tomé y Príncipe'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leona', 'Sierra Leona'), ('Singapur', 'Singapur'), ('Siria', 'Siria'), ('Somalia', 'Somalia'), ('Sri Lanka', 'Sri Lanka'), ('Sudán', 'Sudán'), ('Suecia', 'Suecia'), ('Suiza', 'Suiza'), ('Surinam', 'Surinam'), ('Tayikistán', 'Tayikistán'), ('Tailandia', 'Tailandia'), ('Tanzania', 'Tanzania'), ('Timor Oriental', 'Timor Oriental'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad y Tobago', 'Trinidad y Tobago'), ('Túnez', 'Túnez'), ('Turkmenistán', 'Turkmenistán'), ('Turquía', 'Turquía'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ucrania', 'Ucrania'), ('Uruguay', 'Uruguay'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yibuti', 'Yibuti'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabue', 'Zimbabue')], max_length=50)),
                ('ciudad', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField()),
                ('habilidades', models.TextField()),
                ('experiencia', models.TextField()),
                ('nivel_estudios', models.TextField()),
                ('modalidad_trabajo', models.CharField(choices=[('virtual', 'virtual'), ('presencial', 'presencial'), ('mixto', 'mixto')], max_length=50)),
                ('tipo_contrato', models.CharField(choices=[('termino_fijo', 'Contrato a Término Fijo'), ('termino_indefinido', 'Contrato a Término Indefinido'), ('aprendizaje', 'Contrato de Aprendizaje'), ('obra_labor', 'Contrato por Obra o Labor'), ('tiempo_parcial', 'Contrato a Tiempo Parcial'), ('teletrabajo', 'Contrato de Teletrabajo'), ('temporada', 'Contrato de Temporada'), ('servicios', 'Contrato de Servicios')], default='termino_fijo', max_length=30)),
                ('competencias_tecnicas', models.TextField()),
                ('video_presentacion', models.FileField(upload_to='videos_presentacion_empleo/')),
                ('reclutador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.reclutador_empresa')),
                ('palabras_clave', models.ManyToManyField(to='empleos_reclutador.palabraclave')),
            ],
        ),
    ]
