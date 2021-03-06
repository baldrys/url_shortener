from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

from .models import ShortURL
from .forms import SubmitForm


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):

        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        redirect_url = obj.url

        obj.clicked_times+= 1
        obj.save()

        if not (redirect_url.startswith('http://') or redirect_url.startswith('https://')):
            redirect_url = 'http://' + redirect_url
        return HttpResponseRedirect(redirect_url)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitForm()
        context = {
            "title": "ShortURL",
            "form": form
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitForm(request.POST)
        context = {
            "title": "ShortURL",
            "form": form
        }
        template = "home.html"
        if form.is_valid():
            # print(form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            shortcode = form.cleaned_data.get("short_url")
            if shortcode != '' and shortcode is not None:
                obj = ShortURL(url=new_url, shortcode=shortcode)
                obj.save()
                created = True
            else:
                obj = ShortURL.objects.create(url = new_url)
                # obj, created = ShortURL.objects.get_or_create(url = new_url)
            # kwargs = {'flag': True}
            # obj.save(kwargs)

            context = {
                "object": obj,
                # "created": created,
            }
            # if created:
            #     template = "success.html"
            # else:
            #     template = "already-exists.html"
            template = "success.html"


        return render(request, template, context)
