
import os
import dotenv
from datetime import timedelta
# import django_heroku
import dj_database_url



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    
# SECRET_KEY = '%p8#dko(q2l2d+9-k(f)6w-1p$(*3*y2v#+^ebjxka@og*oocd'

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['learnghb.herokuapp.com', '127.0.0.1']


print('Using production')

# ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # third party
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'corsheaders',

    # All auth
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',

    # local apps
    'accounts',
    'posts',
    'course_content',
    'questions',
    'solutions',
    'lessons',
    'heroes',
    'file_upload'
]
# allauth

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'  # change on production

# JWT settings

REST_USE_JWT = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learngh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'learngh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'learngh',
        'USER': 'agbeko',
        'PASSWORD': os.environ['PASSWORD'],
        'HOST': '*',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# static files source for the project during development

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
# static files source for the project during production

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn', 'media_root')
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                           "static_cdn", "static_root")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# where uploaded files would be kept
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn', 'media_root')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),
                          "static_cdn", "media_root")


CRISPY_TEMPLATE_PACK = 'uni_form'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    # 'JWT_ALGORITHM': 'RS256',
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200'
]
ACCESS_CONTROL_ALLOW_ORIGIN = [
    'http://localhost:4200'
]
ACCESS_CONTROL_ALLOW_CREDENTIAL = True
CORS_ORIGIN_ALLOW_ALL = True

# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# DATABASES['default'] = dj_database_url.config(default='postgres://...')

# django_heroku.settings(locals())

