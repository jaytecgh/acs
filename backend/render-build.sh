#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations

# Run migrations
python manage.py migrate

# Create superuser
python create_superuser.py

# Collect static files (optional but recommended)
python manage.py collectstatic --noinput
