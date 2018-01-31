from rest_framework import serializers

from shortener.models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('pk', 'url', 'shortcode', 'clicked_times', 'creation_date')
        read_only_fields = ('pk', 'clicked_times', 'creation_date')

