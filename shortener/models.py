from django.db import models
from django.conf import settings
# Create your models here.
from django.core.urlresolvers import reverse
from shortener.utils import create_shortcode
from shortener.validators import validate_url
# Пытаемся импортировать из настроек максимальную длину укороченного юрл
# если не удалось, то используем значение по умолчанию
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)



# валидатор url в модели, что бы из админки нельзя было сохранить невалидный url
class ShortURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    clicked_times = models.IntegerField(default=0)
    # is_automatically_generated = models.BooleanField(default=True)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):

        # print('FALG: ', kwargs.get('flag'))
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode})
        return settings.HOST + url_path