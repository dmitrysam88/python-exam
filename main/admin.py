from django.contrib import admin
from main.models import Exam, Question, Answer, Test, Subdivision, Worker

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Test)
admin.site.register(Subdivision)
admin.site.register(Worker)
