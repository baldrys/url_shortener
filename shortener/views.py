from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

from .models import ShortURL
from .forms import SubmitForm

class ShortURLView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitForm()
        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitForm(request.POST)
        context = {
            "title": "Submit URL",
            "form": form
        }
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, "home.html", context)