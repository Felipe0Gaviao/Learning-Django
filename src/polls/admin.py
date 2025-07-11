from django.contrib import admin

# Again with the . imports, at least this time it's coming from somewhere
from .models import Question

# i'm not sure if i like this.
# i'm assuming there's probably a way to replicate this code to work with the progammer's own admin page, if they made one.
#  the parameter is called model_or_iterable, so i'm assuming i don't need to register each model separately.
admin.site.register(Question)
