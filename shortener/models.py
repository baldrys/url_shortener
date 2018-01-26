from django.db import models
from django.conf import settings
# Create your models here.
from shortener.utils import create_shortcode

# Пытаемся импортировать из настроек максимальную длину укороченного юрл
# если не удалось, то используем значение по умолчанию
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortURLManager(models.Manager):

    def refresh_shortcodes(self):
        qs = ShortURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes+=1
        return "New codes made: {0}".format(new_codes)

class ShortURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    clicked_times = models.IntegerField(default=0)
    # is_automatically_generated = models.BooleanField(default=True)

    objects = ShortURLManager()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)