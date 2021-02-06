release: python diploma_project/manage.py makemigrations tours --no-input
release: python diploma_project/manage.py migrate tours --no-input

web: gunicorn diploma_project/diploma_project/wsgi --log-file