from django.contrib import admin
from main.models import Exam, Question, Answer, Test

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Test)
