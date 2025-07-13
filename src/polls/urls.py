from django.urls import path

# Im not sure if i'm a fan of this syntax.
from . import views

app_name = "polls"

# A whole new file just for URL Patterns, i'm not sure if i like it.

# Django seems flexible enough to let the me choose not to do that and instead do it the way that i want.
# Like putting this in the global urls.py and managing everything from there.

# As i'm just following the tutorial, i'm going to continue with this.
# It does look more scalable.
# If this was a real project and it became big enough.
# Having the url patterns separated like this would be nice to deal with.

urlpatterns = [
    path("", views.index, name="index"),
    # Adding the type of the question_id to the route, i'm not completly against that.
    # My problem with this is that problem is, again, it's using strings.
    # It would be cool if it could use the types from the view's function definition.
    # But it would probably break backwards compatibility.
    # Because the functions required for this to work are probably in the more recent versions of python.
    # So i can't see what would be a better way of doing this without breaking backwards compatibility
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
