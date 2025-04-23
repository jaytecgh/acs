"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# ✅ Create superuser only if it doesn't exist
if not User.objects.filter(email="constructionsupplyghstaff2@gmail.com").exists():
    User.objects.create_superuser(
        email="constructionsupplyghstaff2@gmail.com",
        password="@ACS-admin@",  # Change this later in admin
        is_staff=True,
        is_superuser=True
    )
    print("✅ Superuser created on startup")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
