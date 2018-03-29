from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
    '.dlighter.com',
    '.elasticbeanstalk.com',
]
WSGI_APPLICATION = 'config.wsgi.production.application'


DATABASES = secrets_production['DATABASES']
