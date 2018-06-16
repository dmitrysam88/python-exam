from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    number_questions = models.IntegerField(max_length=5)

    def __str__(self):
        return self.name

class Question(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    text = models.TextField()
    right_text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    text = models.TextField()
    right = models.BooleanField()

    def __str__(self):
        return self.text

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    time = models.DateTimeField()
    mark = models.IntegerField(max_length=5)

class Subdivision(models.Model):
    name = models.CharField(max_length=100)


class Werker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.CharField(max_length=25)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)