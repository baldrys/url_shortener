web: gunicorn url_shortener.wsgi --log-file -
worker: python manage.py purge_old_data