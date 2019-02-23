#!/bin/sh

# This file performs some of the necessary commands
# to start the django server properly

# Checking for any model changes (or creating initial migration # files )
eval "./manage.py makemigrations"

# Running a migration files we may have made
eval "./manage.py migrate"

# Checking to see if we've created our superuser for this
# installation
if [ ! -f .user ]; then
  # Creating a default superuser if none exists
  echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
  # Creating the file we use to see if we have a superuser
  touch .user
fi

# Spinning up the development server
eval "./manage.py runserver 0.0.0.0:8123"
