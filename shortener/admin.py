from django.contrib import admin

# Register your models here.
from .models import ShortURL



class ShortURLAdmin(admin.ModelAdmin):
    # fields = ('url', 'shortcode', )
    readonly_fields = ('creation_date', 'clicked_times', )

admin.site.register(ShortURL, ShortURLAdmin)