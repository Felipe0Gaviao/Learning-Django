from django.contrib import admin

# Again with the . imports, at least this time it's coming from somewhere
from .models import Question, Choice


# I'm not sure if this is how it should be, my type checker was complaining about "expected aruments for generic class".
# Loking inside, it doesn't seem to be a Generic Class, maybe it's a very deep inheritance that i can't find where there's a generic class.
# adding "[Question]" to the line, works for the type checker, but running the server gives an error, so i don't know.
class ChoiceInline(admin.TabularInline):  # pyright: ignore[reportMissingTypeArgument]
    model = Choice
    extra = 3


# same thing here
class QuestionAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
