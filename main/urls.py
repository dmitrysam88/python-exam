from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('logout',views.logout),
    path('quest_ans',views.questionAnswer),
    path('testing', views.testing),
    path('choose_exam', views.chooseExam),
    path('check_answer', views.checkAnswer),
    path('show_results', views.showResults),
    path('create_file', views.createFile),
    path('dawnload_questions', views.dawnloadQuestions),
]