import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Models are tables and class variables are columns in the table, i like it.
# Having the database structure being handled in the server makes it easier to change things around.
# Very different from the whole, Client -> Server -> Databae steps.
# Just Client -> Server / Database, i like it.


# i see some of the downsides now.
# i'm not sure if it's the way django is.
# There must exist a more modern way, even if it's not backwards compatible.
class Question(models.Model):
    id: int
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # Found a way :)
    choice_set: models.QuerySet["Choice"]

    def __str__(self):
        return self.question_text

    # I like that i can just make methods like that, it's one of the upsides of having the database logic on the server.

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
