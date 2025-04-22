# create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(email="constructionsupplyghstaff2@gmail.com").exists():
    User.objects.create_superuser(
        email="constructionsupplyghstaff2@gmail.com",
        password="@ACS-admin@",
        full_name="Admin",
        is_staff=True,
        is_superuser=True
    )
    print("✅ Superuser created")
else:
    print("⚠️ Superuser already exists")
