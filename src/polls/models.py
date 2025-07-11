import datetime

from django.db import models
from django.utils import timezone

# Type checking this needed an external "django-types" library


# Models are tables and class variables are columns in the table, i like it.
# Having the database structure being handled in the server makes it easier to change things around.
# Very different from the whole, Client -> Server -> Databae steps.
# Just Client -> Server / Database, i like it.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    # I like that i can just make methods like that, it's one of the upsides of having the database logic on the server.
    # In the future, i'm assuming that i'm going to use this for something.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
