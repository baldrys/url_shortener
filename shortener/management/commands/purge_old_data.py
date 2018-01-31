# purge_old_data.py

import django
django.setup()
from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL
from datetime import datetime, timedelta
from django.utils import timezone
from url_shortener.settings import SHORT_URL_LIFE_TIME

class Command(BaseCommand):
    help = 'Delete short-url record in db older than {0} day(s)'.format(SHORT_URL_LIFE_TIME)

    def handle(self, *args, **options):

        # ShortURL.objects.filter(creation_date__lte=timezone.now() - timedelta(days=SHORT_URL_LIFE_TIME)).delete()
        ShortURL.objects.filter(creation_date__lte=timezone.now() - timedelta(minutes=1)).delete()
        # self.stdout.write('Deleted objects older than 10 days')