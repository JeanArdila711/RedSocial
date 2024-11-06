from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
import openai
import json
from decouple import config
import openai
import json
from django.conf import settings


class RepresentanteLegal(models.Model):
    nombre = models.CharField(max_length=255)
    documento_identidad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class RedesSociales(models.Model):
    facebook = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Redes sociales {self.id}"


class Idiomas(models.TextChoices):
    INGLES = 'ingles', 'ingles'
    ESPANOL = 'espanol', 'espanol'
    CHINO = 'chino', 'chino'
    FRANCES = 'frances', 'frances'
    ALEMAN = 'aleman', 'aleman'
    PORTUGUES = 'portugues', 'portugues'
    ITALIANO = 'italiano', 'italiano'
    ARABE = 'arabe', 'arabe'
    JAPONES = 'japones', 'japones'
    RUSO = 'ruso', 'ruso'
    HOLANDES = 'holandes', 'holandes'
    COREANO = 'coreano', 'coreano'
    SUECO = 'sueco', 'sueco'
    TURCO = 'turco', 'turco'
    HINDI = 'hindi', 'hindi'
    HEBREO = 'hebreo', 'hebreo'
    POLACO = 'polaco', 'polaco'
    GRIEGO = 'griego', 'griego'
    CHECO = 'checo', 'checo'
    DANES = 'danes', 'danes'


class SalarioRango(models.TextChoices):
    rango0 = '500000-1000000', '500,000 - 1,000,000'
    rango1 = '1000000-1500000', '1,000,000 - 1,500,000'
    rango2 = '1500000-2000000', '1,500,000 - 2,000,000'
    rango3 = '2000000-2500000', '2,000,000 - 2,500,000'
    rango4 = '2500000-3000000', '2,500,000 - 3,000,000'
    rango5 = '3000000-3500000', '3,000,000 - 3,500,000'
    rango6 = '3500000-4000000', '3,500,000 - 4,000,000'
    rango7 = '4000000-4500000', '4,000,000 - 4,500,000'
    rango8 = '4500000-5000000', '4,500,000 - 5,000,000'
    rango9 = '5000000-6000000', '5,000,000 - 6,000,000'
    rango10 = '6000000-7000000', '6,000,000 - 7,000,000'
    rango11 = '7000000-8000000', '7,000,000 - 8,000,000'
    rango12 = '8000000-9000000', '8,000,000 - 9,000,000'
    rango13 = '9000000-10000000', '9,000,000 - 10,000,000'
    rango14 = '10000000-12000000', '10,000,000 - 12,000,000'
    rango15 = '12000000-14000000', '12,000,000 - 14,000,000'
    rango16 = '14000000-16000000', '14,000,000 - 16,000,000'
    rango17 = '16000000-18000000', '16,000,000 - 18,000,000'
    rango18 = '18000000-20000000', '18,000,000 - 20,000,000'
    rango19 = '20000000+', 'Más de 20,000,000'


class SectoresLaborales(models.TextChoices):
    ESTILISMO_CUIDADO_PERSONAL = 'estilismo_ciudadopersonal', 'Estilismo y cuidado personal'
    ADMINISTRACION = 'administracion empresarial', 'Administracion Empresarial'
    TECNOLOGIA_DE_LA_INFORMACION = 'tecnologia_de_la_informacion', 'Tecnologia de la Informacion'
    FINANZAS_Y_CONTABILIDAD = 'finanzas_y_contabilidad', 'Finanzas y Contabilidad'
    SALUD = 'salud', 'Salud'
    EDUCACION = 'educacion', 'Educacion'
    INGENIERIA = 'ingenieria', 'Ingenieria'
    MARKETING_Y_PUBLICIDAD = 'marketing_y_publicidad', 'Marketing y Publicidad'
    VENTAS = 'ventas', 'Ventas'
    SERVICIOS_AL_CLIENTE = 'servicios_al_cliente', 'Servicios al Cliente'
    CONSTRUCCION = 'construccion', 'Construccion'
    MANUFACTURA = 'manufactura', 'Manufactura'
    RECURSOS_HUMANOS = 'recursos_humanos', 'Recursos Humanos'
    ARTES_Y_ENTRETENIMIENTO = 'artes_y_entretenimiento', 'Artes y Entretenimiento'
    TURISMO_Y_HOSPITALIDAD = 'turismo_y_hospitalidad', 'Turismo y Hospitalidad'
    TRANSPORTE_Y_LOGISTICA = 'transporte_y_logistica', 'Transporte y Logistica'
    LEGAL = 'legal', 'Legal'
    INVESTIGACION_Y_DESARROLLO = 'investigacion_y_desarrollo', 'Investigacion y Desarrollo'
    ENERGIA_Y_RECURSOS_NATURALES = 'energia_y_recursos_naturales', 'Energia y Recursos Naturales'
    SERVICIOS_PROFESIONALES = 'servicios_profesionales', 'Servicios Profesionales'
    MEDIOS_DE_COMUNICACION = 'medios_de_comunicacion', 'Medios de Comunicacion'
    AGRICULTURA = 'agricultura', 'Agricultura'
    GOBIERNO_Y_ADMINISTRACION_PUBLICA = 'gobierno_y_administracion_publica', 'Gobierno y Administracion Publica'
    CIENCIA_Y_TECNOLOGIA = 'ciencia_y_tecnologia', 'Ciencia y Tecnologia'
    SERVICIOS_SOCIALES = 'servicios_sociales', 'Servicios Sociales'
    MEDIO_AMBIENTE = 'medio_ambiente', 'Medio Ambiente'
    COMERCIO_Y_RETAIL = 'comercio_y_retail', 'Comercio y Retail'


class IndicativoPais(models.TextChoices):
    AFGANISTAN = '+93', 'Afganistán'
    ALBANIA = '+355', 'Albania'
    ALEMANIA = '+49', 'Alemania'
    ANDORRA = '+376', 'Andorra'
    ANGOLA = '+244', 'Angola'
    ANTIGUA_Y_BARBUDA = '+1-268', 'Antigua y Barbuda'
    ARABIA_SAUDITA = '+966', 'Arabia Saudita'
    ARGELIA = '+213', 'Argelia'
    ARGENTINA = '+54', 'Argentina'
    ARMENIA = '+374', 'Armenia'
    AUSTRALIA = '+61', 'Australia'
    AUSTRIA = '+43', 'Austria'
    AZERBAIYAN = '+994', 'Azerbaiyán'
    BAHAMAS = '+1-242', 'Bahamas'
    BAREIN = '+973', 'Baréin'
    BANGLADES = '+880', 'Bangladés'
    BARBADOS = '+1-246', 'Barbados'
    BELGICA = '+32', 'Bélgica'
    BELICE = '+501', 'Belice'
    BENIN = '+229', 'Benín'
    BHUTAN = '+975', 'Bhután'
    BIELORRUSIA = '+375', 'Bielorrusia'
    BIRMANIA = '+95', 'Birmania (Myanmar)'
    BOLIVIA = '+591', 'Bolivia'
    BOSNIA_Y_HERZEGOVINA = '+387', 'Bosnia y Herzegovina'
    BOTSUANA = '+267', 'Botsuana'
    BRASIL = '+55', 'Brasil'
    BRUNEI = '+673', 'Brunéi'
    BULGARIA = '+359', 'Bulgaria'
    BURKINA_FASO = '+226', 'Burkina Faso'
    BURUNDI = '+257', 'Burundi'
    CABO_VERDE = '+238', 'Cabo Verde'
    CAMBOYA = '+855', 'Camboya'
    CAMERUN = '+237', 'Camerún'
    CANADA_ESTADOS_UNIDOS = '+1', 'Canadá | Estados Unidos'
    CATAR = '+974', 'Catar'
    CHAD = '+235', 'Chad'
    CHILE = '+56', 'Chile'
    CHINA = '+86', 'China'
    CHIPRE = '+357', 'Chipre'
    COLOMBIA = '+57', 'Colombia'
    COMORAS = '+269', 'Comoras'
    COREA_DEL_NORTE = '+850', 'Corea del Norte'
    COREA_DEL_SUR = '+82', 'Corea del Sur'
    COSTA_DE_MARFIL = '+225', 'Costa de Marfil'
    COSTA_RICA = '+506', 'Costa Rica'
    CROACIA = '+385', 'Croacia'
    CUBA = '+53', 'Cuba'
    DINAMARCA = '+45', 'Dinamarca'
    DOMINICA = '+1-767', 'Dominica'
    ECUADOR = '+593', 'Ecuador'
    EGIPTO = '+20', 'Egipto'
    EL_SALVADOR = '+503', 'El Salvador'
    EMIRATOS_ARABES_UNIDOS = '+971', 'Emiratos Árabes Unidos'
    ERITREA = '+291', 'Eritrea'
    ESLOVAQUIA = '+421', 'Eslovaquia'
    ESLOVENIA = '+386', 'Eslovenia'
    ESPANA = '+34', 'España'
    ESTONIA = '+372', 'Estonia'
    ETIOPIA = '+251', 'Etiopía'
    FILIPINAS = '+63', 'Filipinas'
    FINLANDIA = '+358', 'Finlandia'
    FIJI = '+679', 'Fiyi'
    FRANCIA = '+33', 'Francia'
    GABON = '+241', 'Gabón'
    GAMBIA = '+220', 'Gambia'
    GEORGIA = '+995', 'Georgia'
    GHANA = '+233', 'Ghana'
    GRANADA = '+1-473', 'Granada'
    GRECIA = '+30', 'Grecia'
    GUATEMALA = '+502', 'Guatemala'
    GUINEA = '+224', 'Guinea'
    GUINEA_BISSAU = '+245', 'Guinea-Bisáu'
    GUINEA_ECUATORIAL = '+240', 'Guinea Ecuatorial'
    GUYANA = '+592', 'Guyana'
    HAITI = '+509', 'Haití'
    HONDURAS = '+504', 'Honduras'
    HUNGRIA = '+36', 'Hungría'
    INDIA = '+91', 'India'
    INDONESIA = '+62', 'Indonesia'
    IRAK = '+964', 'Irak'
    IRAN = '+98', 'Irán'
    IRLANDA = '+353', 'Irlanda'
    ISLANDIA = '+354', 'Islandia'
    ISRAEL = '+972', 'Israel'
    ITALIA = '+39', 'Italia'
    JAMAICA = '+1-876', 'Jamaica'
    JAPON = '+81', 'Japón'
    JORDANIA = '+962', 'Jordania'
    KENIA = '+254', 'Kenia'
    KIRGUISTAN = '+996', 'Kirguistán'
    KIRIBATI = '+686', 'Kiribati'
    KUWAIT = '+965', 'Kuwait'
    LAOS = '+856', 'Laos'
    LETONIA = '+371', 'Letonia'
    LIBANO = '+961', 'Líbano'
    LESOTO = '+266', 'Lesoto'
    LIBERIA = '+231', 'Liberia'
    LIBIA = '+218', 'Libia'
    LIENCHENSTEIN = '+423', 'Liechtenstein'
    LITUANIA = '+370', 'Lituania'
    LUZEMBURGO = '+352', 'Luxemburgo'
    MACEDONIA_DEL_NORTE = '+389', 'Macedonia del Norte'
    MADAGASCAR = '+261', 'Madagascar'
    MALASIA = '+60', 'Malasia'
    MALAWI = '+265', 'Malawi'
    MALDIVAS = '+960', 'Maldivas'
    MALI = '+223', 'Malí'
    MALTA = '+356', 'Malta'
    MARRUECOS = '+212', 'Marruecos'
    MAURICIO = '+230', 'Mauricio'
    MAURITANIA = '+222', 'Mauritania'
    MEXICO = '+52', 'México'
    MICRONESIA = '+691', 'Micronesia'
    MOLDAVIA = '+373', 'Moldavia'
    MONACO = '+377', 'Mónaco'
    MONGOLIA = '+976', 'Mongolia'
    MONTENEGRO = '+382', 'Montenegro'
    MOZAMBIQUE = '+258', 'Mozambique'
    NAMIBIA = '+264', 'Namibia'
    NAURU = '+674', 'Nauru'
    NEPAL = '+977', 'Nepal'
    NICARAGUA = '+505', 'Nicaragua'
    NIGER = '+227', 'Níger'
    NIGERIA = '+234', 'Nigeria'
    NORUEGA = '+47', 'Noruega'
    NUEVA_ZELANDA = '+64', 'Nueva Zelanda'
    OMAN = '+968', 'Omán'
    Paises_Bajos = '+31', 'Países Bajos'
    PAKISTAN = '+92', 'Pakistán'
    PALAU = '+680', 'Palaos'
    PANAMA = '+507', 'Panamá'
    PAPUA_NUEVA_GUINEA = '+675', 'Papúa Nueva Guinea'
    PARAGUAY = '+595', 'Paraguay'
    PERU = '+51', 'Perú'
    POLONIA = '+48', 'Polonia'
    PORTUGAL = '+351', 'Portugal'
    REINO_UNIDO = '+44', 'Reino Unido'
    REP_CENTROAFRICANA = '+236', 'República Centroafricana'
    REP_CHECA = '+420', 'República Checa'
    REP_DOMINICANA = '+1-809, +1-829, +1-849', 'República Dominicana'
    REP_CONGO = '+242', 'República del Congo'
    RUANDA = '+250', 'Ruanda'
    RUMANIA = '+40', 'Rumania'
    RUSIA_KAZAJISTAN = '+7', 'Rusia | Kazajistán'
    SAMOA = '+685', 'Samoa'
    SAN_CRISTOBAL_Y_NIEVES = '+1-869', 'San Cristóbal y Nieves'
    SAN_MARINO = '+378', 'San Marino'
    SAN_VICENTE_Y_LAS_GRANADINAS = '+1-784', 'San Vicente y las Granadinas'
    SANTA_LUCIA = '+1-758', 'Santa Lucía'
    SANTO_TOME_Y_PRINCIPE = '+239', 'Santo Tomé y Príncipe'
    SENEGAL = '+221', 'Senegal'
    SERBIA = '+381', 'Serbia'
    SEYCHELLES = '+248', 'Seychelles'
    SIERRA_LEONA = '+232', 'Sierra Leona'
    SINGAPUR = '+65', 'Singapur'
    SIRIA = '+963', 'Siria'
    SOMALIA = '+252', 'Somalia'
    SRI_LANKA = '+94', 'Sri Lanka'
    SUAZILANDIA = '+268', 'Suazilandia'
    SUDAN = '+249', 'Sudán'
    SUDAFRICA = '+27', 'Sudáfrica'
    SUECIA = '+46', 'Suecia'
    SUIZA = '+41', 'Suiza'
    SURINAM = '+597', 'Surinam'
    TAILANDIA = '+66', 'Tailandia'
    TANZANIA = '+255', 'Tanzania'
    TAYIKISTAN = '+992', 'Tayikistán'
    TIMOR_ORIENTAL = '+670', 'Timor Oriental'
    TOGO = '+228', 'Togo'
    TONGA = '+676', 'Tonga'
    TRINIDAD_Y_TOBAGO = '+1-868', 'Trinidad y Tobago'
    TUNEZ = '+216', 'Túnez'
    TURKMENISTAN = '+993', 'Turkmenistán'
    TURQUIA = '+90', 'Turquía'
    TUVALU = '+688', 'Tuvalu'
    UCRANIA = '+380', 'Ucrania'
    UGANDA = '+256', 'Uganda'
    URUGUAY = '+598', 'Uruguay'
    UZBEKISTAN = '+998', 'Uzbekistán'
    VANUATU = '+678', 'Vanuatu'
    VATICANO = '+379', 'Vaticano'
    VENEZUELA = '+58', 'Venezuela'
    VIETNAM = '+84', 'Vietnam'
    YEMEN = '967', 'Yemen'
    YIBUTI = '+253', 'Yibuti'
    ZAMBIA = '+260', 'Zambia'
    ZIMBABWE = '+263', 'Zimbabue'


class Paises(models.TextChoices):
    AFGANISTAN = 'Afganistán', 'Afganistán'
    ALBANIA = 'Albania', 'Albania'
    ALEMANIA = 'Alemania', 'Alemania'
    ANDORRA = 'Andorra', 'Andorra'
    ANGOLA = 'Angola', 'Angola'
    ANTIGUA_Y_BARBUDA = 'Antigua y Barbuda', 'Antigua y Barbuda'
    ARABIA_SAUDITA = 'Arabia Saudita', 'Arabia Saudita'
    ARGELIA = 'Argelia', 'Argelia'
    ARGENTINA = 'Argentina', 'Argentina'
    ARMENIA = 'Armenia', 'Armenia'
    AUSTRALIA = 'Australia', 'Australia'
    AUSTRIA = 'Austria', 'Austria'
    AZERBAIYAN = 'Azerbaiyán', 'Azerbaiyán'
    BAHAMAS = 'Bahamas', 'Bahamas'
    BAREIN = 'Baréin', 'Baréin'
    BANGLADES = 'Bangladés', 'Bangladés'
    BARBADOS = 'Barbados', 'Barbados'
    BELICE = 'Belice', 'Belice'
    BENIN = 'Benín', 'Benín'
    BIELORRUSIA = 'Bielorrusia', 'Bielorrusia'
    BIRMANIA = 'Birmania', 'Birmania'
    BOLIVIA = 'Bolivia', 'Bolivia'
    BOSNIA_Y_HERZEGOVINA = 'Bosnia y Herzegovina', 'Bosnia y Herzegovina'
    BOTSUANA = 'Botsuana', 'Botsuana'
    BRASIL = 'Brasil', 'Brasil'
    BRUNEI = 'Brunei', 'Brunei'
    BULGARIA = 'Bulgaria', 'Bulgaria'
    BURKINA_FASO = 'Burkina Faso', 'Burkina Faso'
    BURUNDI = 'Burundi', 'Burundi'
    BUTAN = 'Bután', 'Bután'
    CABO_VERDE = 'Cabo Verde', 'Cabo Verde'
    CAMBOYA = 'Camboya', 'Camboya'
    CAMERUN = 'Camerún', 'Camerún'
    CANADA = 'Canadá', 'Canadá'
    CATAR = 'Catar', 'Catar'
    CHAD = 'Chad', 'Chad'
    CHILE = 'Chile', 'Chile'
    CHINA = 'China', 'China'
    CHIPRE = 'Chipre', 'Chipre'
    COLOMBIA = 'Colombia', 'Colombia'
    COMORAS = 'Comoras', 'Comoras'
    CONGO_BRAZZAVILLE = 'Congo (Brazzaville)', 'Congo (Brazzaville)'
    CONGO_KINSHASA = 'Congo (Kinshasa)', 'Congo (Kinshasa)'
    COSTA_RICA = 'Costa Rica', 'Costa Rica'
    CROACIA = 'Croacia', 'Croacia'
    CUBA = 'Cuba', 'Cuba'
    DINAMARCA = 'Dinamarca', 'Dinamarca'
    DOMINICA = 'Dominica', 'Dominica'
    ECUADOR = 'Ecuador', 'Ecuador'
    EGIPTO = 'Egipto', 'Egipto'
    EL_SALVADOR = 'El Salvador', 'El Salvador'
    GUINEA_ECUATORIAL = 'Guinea Ecuatorial', 'Guinea Ecuatorial'
    ERITREA = 'Eritrea', 'Eritrea'
    ESTONIA = 'Estonia', 'Estonia'
    ESWATINI = 'Eswatini', 'Eswatini'
    ESPANA = 'España', 'España'
    ESTADOS_UNIDOS = 'Estados Unidos', 'Estados Unidos'
    FILIPINAS = 'Filipinas', 'Filipinas'
    FINLANDIA = 'Finlandia', 'Finlandia'
    FIJI = 'Fiyi', 'Fiyi'
    FRANCIA = 'Francia', 'Francia'
    GABON = 'Gabón', 'Gabón'
    GAMBIA = 'Gambia', 'Gambia'
    GEORGIA = 'Georgia', 'Georgia'
    GHANA = 'Ghana', 'Ghana'
    GRECIA = 'Grecia', 'Grecia'
    GRANADA = 'Granada', 'Granada'
    GUATEMALA = 'Guatemala', 'Guatemala'
    GUINEA = 'Guinea', 'Guinea'
    GUINEA_BISSAU = 'Guinea-Bisáu', 'Guinea-Bisáu'
    GUYANA = 'Guyana', 'Guyana'
    HAITI = 'Haití', 'Haití'
    HONDURAS = 'Honduras', 'Honduras'
    HUNGRIA = 'Hungría', 'Hungría'
    INDIA = 'India', 'India'
    INDONESIA = 'Indonesia', 'Indonesia'
    IRAN = 'Irán', 'Irán'
    IRAK = 'Irak', 'Irak'
    IRLANDA = 'Irlanda', 'Irlanda'
    ISLANDIA = 'Islandia', 'Islandia'
    ISRAEL = 'Israel', 'Israel'
    ITALIA = 'Italia', 'Italia'
    JAMAICA = 'Jamaica', 'Jamaica'
    JAPON = 'Japón', 'Japón'
    JORDANIA = 'Jordania', 'Jordania'
    KAZAJISTAN = 'Kazajistán', 'Kazajistán'
    KENIA = 'Kenia', 'Kenia'
    KIRGUISTAN = 'Kirguistán', 'Kirguistán'
    KIRIBATI = 'Kiribati', 'Kiribati'
    KOSOVO = 'Kosovo', 'Kosovo'
    LETONIA = 'Letonia', 'Letonia'
    LIBANO = 'Líbano', 'Líbano'
    LIBERIA = 'Liberia', 'Liberia'
    LIBIA = 'Libia', 'Libia'
    LIECHTENSTEIN = 'Liechtenstein', 'Liechtenstein'
    LITUANIA = 'Lituania', 'Lituania'
    LUXEMBURGO = 'Luxemburgo', 'Luxemburgo'
    MADAGASCAR = 'Madagascar', 'Madagascar'
    MALASIA = 'Malasia', 'Malasia'
    MALAWI = 'Malawi', 'Malawi'
    MALDIVAS = 'Maldivas', 'Maldivas'
    MALI = 'Mali', 'Mali'
    MALTA = 'Malta', 'Malta'
    MARRUECOS = 'Marruecos', 'Marruecos'
    MAURICIO = 'Mauricio', 'Mauricio'
    MAURITANIA = 'Mauritania', 'Mauritania'
    MEXICO = 'México', 'México'
    MICRONESIA = 'Micronesia', 'Micronesia'
    MOLDAVIA = 'Moldavia', 'Moldavia'
    MONACO = 'Mónaco', 'Mónaco'
    MONGOLIA = 'Mongolia', 'Mongolia'
    MONTENEGRO = 'Montenegro', 'Montenegro'
    MOZAMBIQUE = 'Mozambique', 'Mozambique'
    NAMIBIA = 'Namibia', 'Namibia'
    NAURU = 'Nauru', 'Nauru'
    NEPAL = 'Nepal', 'Nepal'
    NICARAGUA = 'Nicaragua', 'Nicaragua'
    NIGER = 'Níger', 'Níger'
    NIGERIA = 'Nigeria', 'Nigeria'
    NORUEGA = 'Noruega', 'Noruega'
    NUEVA_ZELANDA = 'Nueva Zelanda', 'Nueva Zelanda'
    OMAN = 'Omán', 'Omán'
    PAKISTAN = 'Pakistán', 'Pakistán'
    PALAU = 'Palau', 'Palau'
    PANAMA = 'Panamá', 'Panamá'
    PAPUA_NUEVA_GUINEA = 'Papúa Nueva Guinea', 'Papúa Nueva Guinea'
    PARAGUAY = 'Paraguay', 'Paraguay'
    PERU = 'Perú', 'Perú'
    POLONIA = 'Polonia', 'Polonia'
    PORTUGAL = 'Portugal', 'Portugal'
    REP_CENTROAFRICANA = 'República Centroafricana', 'República Centroafricana'
    REP_CHECA = 'República Checa', 'República Checa'
    REP_CONGO = 'República del Congo', 'República del Congo'
    RUMANIA = 'Rumanía', 'Rumanía'
    RUSIA = 'Rusia', 'Rusia'
    RUANDA = 'Ruanda', 'Ruanda'
    SAN_CRISTOBAL_Y_NIEVES = 'San Cristóbal y Nieves', 'San Cristóbal y Nieves'
    SANTA_LUCIA = 'Santa Lucía', 'Santa Lucía'
    SAN_MARINO = 'San Marino', 'San Marino'
    SANTO_TOME_Y_PRINCIPE = 'Santo Tomé y Príncipe', 'Santo Tomé y Príncipe'
    SENEGAL = 'Senegal', 'Senegal'
    SERBIA = 'Serbia', 'Serbia'
    SEYCHELLES = 'Seychelles', 'Seychelles'
    SIERRA_LEONA = 'Sierra Leona', 'Sierra Leona'
    SINGAPUR = 'Singapur', 'Singapur'
    SIRIA = 'Siria', 'Siria'
    SOMALIA = 'Somalia', 'Somalia'
    SRI_LANKA = 'Sri Lanka', 'Sri Lanka'
    SUDAN = 'Sudán', 'Sudán'
    SUECIA = 'Suecia', 'Suecia'
    SUIZA = 'Suiza', 'Suiza'
    SURINAM = 'Surinam', 'Surinam'
    TADJIKISTAN = 'Tayikistán', 'Tayikistán'
    TAILANDIA = 'Tailandia', 'Tailandia'
    TANZANIA = 'Tanzania', 'Tanzania'
    TIMOR_ORIENTAL = 'Timor Oriental', 'Timor Oriental'
    TOGO = 'Togo', 'Togo'
    TONGA = 'Tonga', 'Tonga'
    TRINIDAD_Y_TOBAGO = 'Trinidad y Tobago', 'Trinidad y Tobago'
    TUNEZ = 'Túnez', 'Túnez'
    TURKMENISTAN = 'Turkmenistán', 'Turkmenistán'
    TURQUIA = 'Turquía', 'Turquía'
    TUVALU = 'Tuvalu', 'Tuvalu'
    UGANDA = 'Uganda', 'Uganda'
    UCRANIA = 'Ucrania', 'Ucrania'
    URUGUAY = 'Uruguay', 'Uruguay'
    VANUATU = 'Vanuatu', 'Vanuatu'
    VENEZUELA = 'Venezuela', 'Venezuela'
    VIETNAM = 'Vietnam', 'Vietnam'
    YIBUTI = 'Yibuti', 'Yibuti'
    YEMEN = 'Yemen', 'Yemen'
    ZAMBIA = 'Zambia', 'Zambia'
    ZIMBABUE = 'Zimbabue', 'Zimbabue'


class UserManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, nombre, password, **extra_fields)


class ExperienciaLaboral(models.Model):
    aspirante = models.ForeignKey('Aspirante', on_delete=models.CASCADE, related_name='experiencias')
    titulo_puesto = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)  # Puede estar en curso
    descripcion = models.TextField()


class FormacionAspirante(models.Model):
    aspirante = models.ForeignKey('Aspirante', on_delete=models.CASCADE, related_name='formaciones')
    titulo = models.CharField(max_length=255)
    institucion = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.titulo} en {self.institucion}"


class IdiomaAspirante(models.Model):
    aspirante = models.ForeignKey('Aspirante', on_delete=models.CASCADE, related_name='idiomas')
    idioma = models.CharField(max_length=30, choices=Idiomas.choices, null=True, blank=True)


class TipoUsuario(models.TextChoices):
    ASPIRANTE = 'aspirante', 'Aspirante'
    RECLUTADOR = 'reclutador', 'Reclutador'


class User(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    documento_identidad = models.CharField(max_length=20)
    indicativo_pais = models.CharField(max_length=50, choices=IndicativoPais.choices)
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=50, choices=Paises.choices)
    ciudad = models.CharField(max_length=100)
    foto_perfil = models.ImageField(upload_to='profile_photos/', default='profile_photos/default_profile.jpg',
                                        null=True, blank=True)
    tipo_usuario = models.CharField(max_length=10, choices=TipoUsuario.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email


class Reclutador_empresa(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=255)
    NIT = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    mision = models.TextField()
    vision = models.TextField()
    cantidad_empleados = models.IntegerField()
    sede_principal = models.CharField(max_length=255)
    representante_legal = models.ForeignKey(RepresentanteLegal, on_delete=models.CASCADE)
    registro_camara_comercio = models.FileField(upload_to='registros_camara_comercio/')
    logo = models.ImageField(upload_to='logo_empresas/', default='logo_empresas/Logotipo_empresa.png',
                                    null=True, blank=True)
    palabras_clave = models.TextField(blank=True, null=True)
    embeddings = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Llama a set_embeddings antes de guardar el objeto
        self.set_embeddings_edit_save()
        super().save(*args, **kwargs)  # Llama al método save original


    def set_embeddings_edit_save(self):
        """Genera y almacena el embedding para la empresa."""
        # Concatenar todos los campos relevantes en un solo texto
        texto_completo = (
            f"{self.mision} "
            f"{self.descripcion if self.descripcion else ''} "
            f"{self.vision} "
            f"{self.palabras_clave if self.palabras_clave else ''}"
        )

        openai.api_key = settings.OPENAI_API_KEY

        # Generar embeddings con OpenAI
        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = response.data[0].embedding
            self.embeddings = json.dumps(embedding_data)  # Almacenar como un único embedding
            print(f'el {self.nombre_empresa} se modifico el embbedding')

        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')

    def set_embeddings(self):
        """Genera y almacena el embedding para la empresa."""
        # Concatenar todos los campos relevantes en un solo texto
        texto_completo = (
            f"{self.mision} "
            f"{self.descripcion if self.descripcion else ''} "
            f"{self.vision} "
            f"{self.palabras_clave if self.palabras_clave else ''}"
        )

        openai.api_key = settings.OPENAI_API_KEY

        # Generar embeddings con OpenAI
        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = response.data[0].embedding
            self.embeddings = json.dumps(embedding_data)  # Almacenar como un único embedding
            self.save()
        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')

    def __str__(self):
        return self.nombre_empresa


class Aspirante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    hoja_vida = models.FileField(upload_to='hojas_de_vida/')
    descripcion = models.TextField()
    objetivos = models.TextField()
    sector_laboral = models.CharField(max_length=50, choices=SectoresLaborales.choices)
    gustos_intereses = models.TextField()
    salario = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='COP',  # Moneda predeterminada para Colombia
        currency_choices=[
            ('COP', 'Peso colombiano (COP)'),  # Empleos locales
            ('USD', 'Dólar estadounidense (USD)'),  # Empleos virtuales (EE.UU.)
            ('EUR', 'Euro (EUR)'),  # Empleos virtuales (Europa)
            ('GBP', 'Libra esterlina (GBP)'),  # Empleos virtuales (Reino Unido)
            ('CAD', 'Dólar canadiense (CAD)'),  # Empleos virtuales (Canadá)
            ('AUD', 'Dólar australiano (AUD)'),  # Empleos virtuales (Australia)
            ('BTC', 'Bitcoin (BTC)'),  # Criptomonedas
            ('ETH', 'Ethereum (ETH)'),  # Criptomonedas
        ]
    )
    MODALIDAD_TRABAJO = [('virtual', 'virtual'), ('presencial', 'presencial'), ('mixto', 'mixto'), ('cualquiera', 'cualquiera')]
    modalidad_trabajo = models.CharField(max_length=50, choices=MODALIDAD_TRABAJO)
    disponibilidad_de_empezar = models.DateField()
    disponibilidad_viajar = models.BooleanField(default=False)
    proyectos = models.FileField(upload_to='proyectos/', blank=True, null=True)
    competencias_tecnicas = models.TextField()
    habilidades_blandas = models.TextField()
    palabras_clave = models.TextField(blank=True, null=True)
    redes_sociales = models.OneToOneField(RedesSociales, on_delete=models.CASCADE, null=True, blank=True)
    idioma_natal = models.CharField(max_length=20, choices=Idiomas.choices)  # Almacena idiomas y niveles
    video_presentacion = models.FileField(upload_to='videos_presentacion/')
    embeddings = models.TextField(blank=True, null=True)  # Para almacenar embeddings en formato JSON

    def save(self, *args, **kwargs):
        # Llama a set_embeddings antes de guardar el objeto
        self.set_embeddings_edit_save()
        super().save(*args, **kwargs)  # Llama al método save original

    def set_embeddings_edit_save(self):
        """Genera y almacena el embedding para el aspirante."""
        # Concatenar todos los campos relevantes en un solo texto
        texto_completo = (
            f"{self.descripcion} "
            f"{self.gustos_intereses} "
            f"{self.competencias_tecnicas} "
            f"{self.habilidades_blandas} "
            f"{self.palabras_clave}"
        )

        openai.api_key = settings.OPENAI_API_KEY

        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = response.data[0].embedding
            self.embeddings = json.dumps(embedding_data)  # Almacenar como un único embedding
        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')

    def set_embeddings(self):
        """Genera y almacena el embedding para el aspirante."""
        # Concatenar todos los campos relevantes en un solo texto
        texto_completo = (
            f"{self.descripcion} "
            f"{self.gustos_intereses} "
            f"{self.competencias_tecnicas} "
            f"{self.habilidades_blandas} "
            f"{self.palabras_clave}"
        )

        openai.api_key = settings.OPENAI_API_KEY

        response = openai.embeddings.create(
            input=texto_completo,
            model="text-embedding-ada-002"
        )

        try:
            embedding_data = response.data[0].embedding
            self.embeddings = json.dumps(embedding_data)  # Almacenar como un único embedding
            self.save()
        except AttributeError as e:
            print(f'Error al acceder a los embeddings: {e}')
    def __str__(self):
        return self.usuario.nombre

