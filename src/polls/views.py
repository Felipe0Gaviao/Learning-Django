from django.db.models import F
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"


def vote(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # I was trying to understando from where django is getting choice_set, because my type checker cannot find it
        # After a quick search, i found this:
        # https://stackoverflow.com/questions/2048777/what-is-choice-set-in-this-django-app-tutorial
        # aparently django creates this "choice_set" the moment a ForeignKey was created inside the Choice Model
        # So every time a Foreing key is created pointing to a specific class:
        #    a new <classname>_set method is created in the class that the ForeignKey is pointing to.
        # I really don't like this, to be dynamically creating methods at run-time.
        # I'm not sure if it's by design, but i'm assuming that from now on i will just have to disable my type checker.
        # There must be a better way, but for now i will go along with the tutorial without it.
        selected_choice: Choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
