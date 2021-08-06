from .base import *
from .ckeditor import *
from .email import *

ALLOWED_HOSTS = [
    'www.michael-patterson.com', 
    'young-savannah-60236.herokuapp.com',
]

# SSL/HTTPS
# https://docs.djangoproject.com/en/3.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = True

CORS_ORIGIN_WHITELIST = (
    r"^https://\w+\.michael-patterson\.com$",
    'https://young-savannah-60236.herokuapp.com'
)