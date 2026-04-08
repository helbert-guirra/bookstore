"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")

# Roda migrations automaticamente ao iniciar
call_command('migrate', '--run-syncdb')

application = get_wsgi_application()
