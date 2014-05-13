import dj_database_url
import os
BASE_DIR = lambda *x: os.path.join(os.path.dirname(os.path.dirname(__file__)), *x)

SECRET_KEY = os.environ['S3_KEY']
DEBUG = os.environ['DEBUG']

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

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

AUTH_USER_MODEL = 'users.Customer'

DATABASES = {
    'default': dj_database_url.config()
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


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

TEMPLATE_DIRS = [BASE_DIR('templates')]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




