from django.http import HttpResponse, HttpRequest


# Added HttpRequest with the tutortial's HttpResponse so that i can type check this.
# I do like that it's very easy to just return a Response like that.


def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the polls index.")
