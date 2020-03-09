"""
Django settings for access4all project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import dj_database_url
import os
import sentry_sdk

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, required=True):
    if required:
        try:
            return os.environ[var_name]
        except KeyError:
            raise ImproperlyConfigured(
                f"The '{var_name}' environment variable must be set."
            )
    else:
        return os.environ.get(var_name)


SECRET_KEY = get_env_variable("SECRET_KEY")

# Sentry integration
SENTRY_DSN = get_env_variable("SENTRY_DSN", required=False)
if SENTRY_DSN is not None:
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

# FIXME: this should eventually be provided by some env var
ALLOWED_HOSTS = [
    "access4all.osc-fr1.scalingo.io",
    "access4all.beta.gouv.fr",
]

# Static files
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Application definition

INSTALLED_APPS = [
    "django_extensions",
    "nested_admin",
    "import_export",
    "reset_migrations",
    "django_admin_listfilter_dropdown",
    "erp.apps.ErpConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "django.contrib.postgres",
    "logentry_admin",
    "django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "https://access4all.beta.gouv.fr",
    "http://localhost:8000",
    "http://localhost:3000",
]
CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
]

ROOT_URLCONF = "access4all.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "access4all.wsgi.application"


# Database connection
# see https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# see https://doc.scalingo.com/languages/python/django/start#configure-the-database-access
# see https://pypi.org/project/dj-database-url/ for options management
database_url = os.environ.get(
    "DATABASE_URL", "postgres://access4all:access4all@localhost/access4all"
)
DATABASES = {"default": dj_database_url.config()}
DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "fr"
TIME_ZONE = "Europe/Paris"
DATETIME_FORMAT = "Y-m-d, H:i:s"
USE_I18N = True
USE_L10N = False
USE_TZ = True

# Email sending

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Cache
CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache",}
}

# Local settings
try:
    from .local_settings import *
except ImportError as e:
    pass
