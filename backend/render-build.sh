#!/usr/bin/env bash
# This runs automatically after your app deploys on Render

python manage.py makemigrations
python manage.py migrate

# Optional: create default superuser if it doesn't exist
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='constructionsupplyghstaff2@gmail.com').exists() or User.objects.create_superuser('constructionsupplyghstaff2@gmail.com', '@ACS-admin@')" | python manage.py shell
