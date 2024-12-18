"""
Django settings for redSocialMagneto project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#ytvu9a#unnxvegn=pu0rk@2-)g-v*)asc4#^i2pflo5@gx9v3'

from decouple import config


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'empleos_reclutador',
    'buscador_reclutador',
    'buscador_aspirante',
    'MensajeriaInterna',
    'grupos_interes'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'redSocialMagneto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'redSocialMagneto/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'redSocialMagneto.wsgi.application'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "redSocialMagneto/static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

CURRENCIES = ('COP', 'USD', 'EUR', 'GBP', 'CAD', 'AUD', 'BTC', 'ETH')
CURRENCY_CHOICES = [
    ('COP', 'Peso colombiano (COP)'),
    ('USD', 'Dólar estadounidense (USD)'),
    ('EUR', 'Euro (EUR)'),
    ('GBP', 'Libra esterlina (GBP)'),
    ('CAD', 'Dólar canadiense (CAD)'),
    ('AUD', 'Dólar australiano (AUD)'),
    ('BTC', 'Bitcoin (BTC)'),
    ('ETH', 'Ethereum (ETH)'),
]

CURRENCY_RATES = {
    'COP': 1,
    'USD': 4000,  # Ejemplo: 1 USD = 4000 COP
    'EUR': 4600,  # Ejemplo: 1 EUR = 4600 COP
    'GBP': 5200,  # Ejemplo: 1 GBP = 5200 COP
    'CAD': 3000,  # Ejemplo: 1 CAD = 3000 COP
    'AUD': 2900,  # Ejemplo: 1 AUD = 2900 COP
    'BTC': 140000000,  # Ejemplo: 1 BTC = 140,000,000 COP
    'ETH': 9000000,    # Ejemplo: 1 ETH = 9,000,000 COP
}

