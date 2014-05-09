"""
Django settings for ipharmProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = lambda *x: os.path.join(os.path.dirname(os.path.dirname(__file__)), *x)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g9(#%1jfk*7)i)652z5%cvz@@gsz@!#c$k@(kx63t%s78gl2o)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

# Template Processors
# Template Processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "django.core.context_processors.csrf",
    "django.contrib.auth.context_processors.auth",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventories',
    'pharmacies',
    'users',
    'south',
)
#backends
# AUTHENTICATION_BACKENDS = (
#     'django_facebook.auth_backends.FacebookBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ipharmProject.urls'

WSGI_APPLICATION = 'ipharmProject.wsgi.application'

#Auth
# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'
AUTH_USER_MODEL =  'users.Customer'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ipharm',
        'USER': 'postgres',
        'PASSWORD': 'alfred',
        'HOST': 'localhost',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

ROOT_URL = '/user/'
LOGIN_URL = ROOT_URL + 'login/'
MEDIA_URL = ROOT_URL + 'media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = BASE_DIR('pic_folder/')
STATICFILES_DIRS = (
    BASE_DIR('static/'),
)

#Templates
TEMPLATE_DIRS = [BASE_DIR('templates')]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
