from django.contrib.auth import get_user_model

User = get_user_model()

# Cambia los datos aquí si deseas usar otros
USERNAME = "admin"
EMAIL = "admin@user.com"
PASSWORD = "admin1234"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("✅ Superusuario creado.")
else:
    print("ℹ️ El superusuario ya existe.")
