#!/usr/bin/env python
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    import dotenv

    dotenv.read_dotenv(os.path.join(BASE_DIR, '.env'))

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "naboj.settings.development"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
