import os, sys

PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIR, 'apps'),)
PUBLIC_DIR = os.path.join(PROJECT_DIR, '..', '..', 'public')

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Traceback ME', '7fbmvu5vo@api.traceback.me'),
)

DEFAULT_FROM_EMAIL='info@djangostars.com'
SERVER_EMAIL='info@djangostars.com'

MANAGERS = ADMINS

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static_collected')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'seva.middleware.QueryCountDebugMiddleware'
)

ROOT_URLCONF = 'seva.urls'

WSGI_APPLICATION = 'seva.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, 'fixtures'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'tastypie',
    'profiles',
    'technologies',
    'evaluations',
    'projects',
    'gravatar',
    'djrill'
)

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
MANDRILL_API_KEY = "mVHZ5n7QVBEJX17YYg3MYQ"

AUTH_PROFILE_MODULE = 'profiles.Profile'

TASTYPIE_FULL_DEBUG = True
TASTYPIE_DEFAULT_FORMATS = ['json',]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
try:
    from .settings_local import *
except:
    pass
