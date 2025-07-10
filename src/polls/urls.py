from django.urls import path

# Im not sure if i'm a fan of this syntax.
from . import views

# A whole new file just for URL Patterns, i'm not sure if i like it.

# Django seems flexible enough to let the me choose not to do that and instead do it the way that i want.
# Like putting this in the global urls.py and managing everything from there.

# As i'm just following the tutorial, i'm going to continue with this.
# It does look more scalable.
# If this was a real project and it became big enough.
# Having the url patterns separated like this would be nice to deal with.

urlpatterns = [path("", views.index, name="index")]
