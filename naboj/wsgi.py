"""
WSGI config for naboj project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv.read_dotenv(os.path.join(BASE_DIR, '.env'))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "shootube.naboj.development"
)

application = get_wsgi_application()
