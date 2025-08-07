#!/usr/bin/env bash
echo "==> Ejecutando migraciones..."
python manage.py migrate --noinput

echo "==> Creando superusuario si no existe..."
echo "from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

