from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Theme, Exam

def home(request):
    return render(request, 'app/home.html')

def login(request):
    return render(request, 'app/login.html')

def sign_up(request):
    return render(request, 'app/sign-up.html')

def exams(request):
    exams = Exam.objects.all().order_by('-date_created')
    context = {'exams': exams}
    return render(request, 'app/exams.html', context)

def exam(request, id):
    exam = Exam.objects.get(id=id)

    if exam:
        context = {'exam': exam}

    return render(request, 'app/exam.html', context)

def feedback(request, id):
    exam = Exam.objects.get(id=id)
    questions = exam.question_set.all()
    
    # Obtenha as respostas submetidas
    choices_submitted = {f'question{i+1}': request.POST.get(f'question{i+1}') for i in range(len(questions))}
    
    # Inicialize um dicionário para armazenar o status de cada pergunta
    question_status = {}

    for question in questions:
        # Obtenha a resposta correta para a pergunta
        correct_choice = question.choices_set.filter(is_correct=True).first()
        submitted_answer = choices_submitted.get(f'question{question.id}')
        
        if correct_choice and submitted_answer == correct_choice.text:
            question_status[question.id] = 'correct'
        else:
            question_status[question.id] = 'incorrect'
    
    context = {
        'exam': exam,
        'question_status': question_status,
        'choices_submitted': choices_submitted,
    }
    
    return render(request, 'app/feedback.html', context)

def my_exams(request):
    return render(request, 'app/my-exams.html')

def my_exam(request):
    return render(request, 'app/my-exam.html')

def create_exam(request):
    if request.method == 'POST':
        id_theme = request.POST.get('theme')
        choices_title = request.POST.get('title')

        if id_theme and choices_title:
            theme = Theme.objects.get(id=id_theme)
            
            exam = Exam.objects.create(
                theme=theme,
                title=choices_title
            )
            
            return redirect(reverse('exams'))
                
    themes = Theme.objects.all()
    context = {'themes': themes}
    return render(request, 'app/create-exam.html', context)

def create_question(request):
    return render(request, 'app/create-question.html')

def create_choice(request):
    return render(request, 'app/create-choice.html')

def edit_exam(request):
    return render(request, 'app/edit-exam.html')

def edit_question(request):
    return render(request, 'app/edit-question.html')

def edit_choice(request):
    return render(request, 'app/edit-choice.html')