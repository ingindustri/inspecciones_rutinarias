"""
WSGI config for inspecciones_rutinarias project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inspecciones_rutinarias.settings')

application = get_wsgi_application()

# Ejecutar migrate automáticamente SOLO si las apps ya están listas
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    # Evita que Render se bloquee si falla migrate
    print(f"Error ejecutando migrate: {e}")

