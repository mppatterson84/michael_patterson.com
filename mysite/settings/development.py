from .base import *
from .ckeditor import *
from .email import *

ALLOWED_HOSTS = ['*']

# SSL/HTTPS
# https://docs.djangoproject.com/en/3.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = False

# sessions
# https://docs.djangoproject.com/en/3.2/topics/http/sessions/
# SESSION_COOKIE_SAMESITE = 'None'
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://192.168.1.25:3000',
    'http://192.168.1.25:8000',
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://192.168.1.25:3000',
    'http://192.168.1.25:8000',
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]