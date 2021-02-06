release: python manage.py makemigrations tours --no-input
release: python manage.py migrate tours --no-input

web: gunicorn diploma_project/wsgi --log-file