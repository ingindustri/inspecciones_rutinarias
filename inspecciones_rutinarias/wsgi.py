"""
WSGI config for inspecciones_rutinarias project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inspecciones_rutinarias.settings')

django.setup()

# Ejecuta migraciones y collectstatic automáticamente
call_command('migrate')
call_command('collectstatic', '--noinput')

application = get_wsgi_application()
