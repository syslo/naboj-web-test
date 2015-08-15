from .common import *


DEBUG = False

ALLOWED_HOSTS = list(os.environ.get(
    'DJANGO_ALLOWED_HOSTS',
    'localhost'
).split(','))
