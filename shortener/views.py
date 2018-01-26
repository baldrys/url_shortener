from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

from .models import ShortURL


class ShortURLView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)