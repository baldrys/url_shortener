import django
django.setup()

from apscheduler.schedulers.blocking import BlockingScheduler
from shortener.models import ShortURL
from datetime import datetime, timedelta
from django.utils import timezone
# from url_shortener.settings import SHORT_URL_LIFE_TIME


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    ShortURL.objects.filter(creation_date__lte=timezone.now() - timedelta(minutes=1)).delete()


sched.start()
