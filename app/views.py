from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def sign_up(request):
    return render(request, 'app/sign-up.html')

def exams(request):
    return render(request, 'app/exams.html')

def exam(request):
    return render(request, 'app/exam.html')

def feedback(request):
    return render(request, 'app/feedback.html')