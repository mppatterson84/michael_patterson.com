from .base import *
from .ckeditor import *
from .email import *

ALLOWED_HOSTS = [
    '.michael-patterson.com',
    'www.michael-patterson.com',
    'young-savannah-60236.herokuapp.com',
]

# SSL/HTTPS
# https://docs.djangoproject.com/en/3.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True

# sessions
# https://docs.djangoproject.com/en/3.2/topics/http/sessions/
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True

CSRF_COOKIE_DOMAIN = '.michael-patterson.com'


CORS_ALLOWED_ORIGIN_REGEXES = (
    r"^https://\w+\.michael-patterson\.com$",
    r"^https://\w+\.michael-patterson\.com$",
)

CORS_ALLOWED_ORIGINS = [
    'https://www.michael-patterson.com',
    'https://young-savannah-60236.herokuapp.com',
    'https://tasks-app4739308573.netlify.app/',
]

CSRF_TRUSTED_ORIGINS = [
    'www.michael-patterson.com',
    'tasks.michael-patterson.com',
    'young-savannah-60236.herokuapp.com',
    'tasks-app4739308573.netlify.app',
]