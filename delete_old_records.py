from shortener.models import ShortURL
from datetime import datetime, timedelta
from django.utils import timezone


ShortURL.objects.filter(creation_date__lte=timezone.now() - timedelta(minutes=1)).delete()
