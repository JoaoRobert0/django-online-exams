from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('exams', views.exams, name='exams'),
    path('exam', views.exam, name='exam'),
    path('feedback', views.feedback, name='feedback'),
    path('my-exams', views.my_exams, name='my-exams'),
    path('my-exam', views.my_exam, name='my-exam'),
]