from django.shortcuts import render
from .models import (
    PresentationsCategory, CaseStudyCategory, ListeningCategory,
    IndependentWorkCategory, AssignmentsCategory, Question, Author
)
import random

def homepage(request):
    presentations = PresentationsCategory.objects.all()
    casestudies = CaseStudyCategory.objects.all()
    listenings = ListeningCategory.objects.all()
    independents = IndependentWorkCategory.objects.all()
    assignments = AssignmentsCategory.objects.all()
    questions = Question.objects.all()
    authors = Author.objects.all()

    context = {
        'presentations_count': presentations.count(),
        'casestudy_count': casestudies.count(),
        'listening_count': listenings.count(),
        'independent_count': independents.count(),
        'assignments_count': assignments.count(),
        'questions_count': questions.count(),
        'authors_count': authors.count(),
        'total_videos': presentations.count() + casestudies.count() + independents.count() + assignments.count(),
        'total_audios': listenings.count(),
    }
    return render(request, 'home.html', context)


def presentations_list(request):
    presentations = PresentationsCategory.objects.all()
    return render(request, 'presentations_list.html', {'presentations': presentations})


def casestudy_list(request):
    casestudies = CaseStudyCategory.objects.all()
    return render(request, 'casestudy_list.html', {'casestudies': casestudies})


def listening_list(request):
    listenings = ListeningCategory.objects.all()
    return render(request, 'listening_list.html', {'listenings': listenings})


def independent_list(request):
    independents = IndependentWorkCategory.objects.all()
    return render(request, 'independent_detail.html', {'independents': independents})


def assignments_list(request):
    assignments = AssignmentsCategory.objects.all()
    return render(request, 'assignments_list.html', {'assignments': assignments})






def quiz_list(request):
    questions = list(
        Question.objects.all()
    )
    random.shuffle(questions)
    questions = questions[:15]

    letters = ['A', 'B', 'C', 'D']
    context = {
        'questions': questions,
        'total_questions': len(questions),
        'letters': letters,
    }
    return render(request, 'quiz_list.html', context)

def about(request):
    return render(request, 'about.html')
def courses(request):
    return render(request, 'courses.html')
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_admin(request):
    User = get_user_model()

    if User.objects.filter(username="admin").exists():
        return HttpResponse("Admin already exists")

    User.objects.create_superuser(
        username="admin",
        email="admin@gmail.com",
        password="admin12345"
    )
    return HttpResponse("Superuser created")
