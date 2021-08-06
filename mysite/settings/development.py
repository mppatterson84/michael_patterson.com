from .base import *
from .ckeditor import *
from .email import *

ALLOWED_HOSTS = ['*']

# SSL/HTTPS
# https://docs.djangoproject.com/en/3.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = False

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000'
)
