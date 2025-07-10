from django.contrib import admin
from django.urls import path, include

# From polls/urls.py.
# This is really interesting, i like it here.

# I don't like that "polls.urls" is a string, it would be nice to have autocompletion here.
# And it being a string does not allow for that possibility

# im not sure if could be possible with importlib, but maybe.

urlpatterns = [path("polls/", include("polls.urls")), path("admin/", admin.site.urls)]
