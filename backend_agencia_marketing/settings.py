from pathlib import Path
import os

from pathlib import Path

# ... otras configuraciones

BASE_DIR = Path(__file__).resolve().parent.parent # Corregido: '__file__' en lugar de '_file_'
# ... el resto de tu archivo settings.py

SECRET_KEY = 'django-insecure-ly2j!2lr_k=7%9v8g8km@bxnkc9y&$q6&%yt-@$fu$@-q%m=vm'

DEBUG = True
ALLOWED_HOSTS = []

# ... (código anterior)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # CAMBIO AQUÍ:
    'app_proyectos', 
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

ROOT_URLCONF = 'backend_agencia_marketing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend_agencia_marketing.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
# CAMBIO AQUÍ:
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'app_proyectos/static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'