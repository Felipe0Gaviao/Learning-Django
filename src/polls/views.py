from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render
from .models import Question

# Added HttpRequest with the tutortial's HttpResponse so that i can type check this.
# I do like that it's very easy to just return a Response like that.


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Changing this part to use f-strings instead of %s.
# They are still using it in the tutorial, as of the day that this was commited
# I'm assuming that's for better backwards compatibility.
# I'm using python 3.12, so i can and will use the more modern way of string concatenation
def detail(request: HttpRequest, question_id: int):
    # Why is the parameter for this function call called "klass" instead of "class"?
    # Something that i need to look into after finishing the tutortial if it's not informed during it.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}")
