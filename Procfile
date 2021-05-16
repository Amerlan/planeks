release: python manage.py migrate

django: gunicorn core.wsgi --log-file -

celery: celery -A core worker -l info