# flake8: noqa
from .settings import *

DEBUG = True

SITE_HOST = "localhost"
SITE_ROOT_URL = f"http://testserver"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

TEMPLATES[0]["OPTIONS"]["debug"] = True
TEMPLATES[0]["OPTIONS"]["context_processors"].insert(0, "django.template.context_processors.debug")

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
