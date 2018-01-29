
from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^(?P<pk>[0-9]+)/$', DetailsShortURLView.as_view()),
    url(r'^shorturl/$', CreateShorturlView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)