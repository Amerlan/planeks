release: python manage.py migrate

django: gunicorn djheroku.wsgi --log-file -

celery: celery -A core worker -l info