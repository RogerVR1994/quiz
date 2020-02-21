from django.contrib import admin

from .models import Question, User, Quiz

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Quiz)