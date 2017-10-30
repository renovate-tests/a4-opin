from os import environ

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += [
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

ALLOWED_HOSTS = [
    'dev-env.igharuux97.eu-central-1.elasticbeanstalk.com',
    'localhost',
]

SECRET_KEY = environ['DJANGO_SECRET_KEY']
