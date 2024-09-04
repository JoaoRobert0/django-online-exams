from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('exams', views.exams, name='exams'),
    path('exam/<int:id>', views.exam, name='exam'),
    path('feedback', views.feedback, name='feedback'),
    path('my-exams', views.my_exams, name='my-exams'),
    path('my-exam', views.my_exam, name='my-exam'),
    path('create-exam', views.create_exam, name='create-exam'),
    path('create-question', views.create_question, name='create-question'),
    path('create-choice', views.create_choice, name='create-choice'),
    path('edit-exam', views.edit_exam, name='edit-exam'),
    path('edit-question', views.edit_question, name='edit-question'),
    path('edit-choice', views.edit_choice, name='edit-choice'),
]