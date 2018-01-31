web: gunicorn url_shortener.wsgi --log-file -
clock: python clock.py
worker: python manage.py purge_old_data