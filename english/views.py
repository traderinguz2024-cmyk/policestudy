from django.shortcuts import render
from .models import (
    PresentationsCategory, CaseStudyCategory, ListeningCategory,
    IndependentWorkCategory, AssignmentsCategory, Question, Author
)
import random


def build_course_cards():
    presentations_count = PresentationsCategory.objects.count()
    casestudy_count = CaseStudyCategory.objects.count()
    listening_count = ListeningCategory.objects.count()
    independent_count = IndependentWorkCategory.objects.count()
    assignments_count = AssignmentsCategory.objects.count()
    questions_count = Question.objects.count()

    return [
        {
            "title": "Presentations",
            "description": "Professional taqdimot ko'nikmalarini rivojlantirish uchun materiallar.",
            "count": presentations_count,
            "count_label": "ta fayl",
            "category": "video",
            "duration": "~2 soat",
            "difficulty": "Beginner",
            "badge": "Video",
            "url_name": "presentations",
            "icon": "presentation",
        },
        {
            "title": "Case Study",
            "description": "Real huquqiy vaziyatlar asosida fikrlash va tahlil qilish mashqlari.",
            "count": casestudy_count,
            "count_label": "ta fayl",
            "category": "reading",
            "duration": "~3 soat",
            "difficulty": "Intermediate",
            "badge": "O'qish",
            "url_name": "casestudy",
            "icon": "case-study",
        },
        {
            "title": "Listening",
            "description": "Audio darslar va tinglab tushunishni kuchaytiradigan materiallar.",
            "count": listening_count,
            "count_label": "ta audio",
            "category": "audio",
            "duration": "~1 soat",
            "difficulty": "Beginner",
            "badge": "Audio",
            "url_name": "listening",
            "icon": "listening",
        },
        {
            "title": "Independent Work",
            "description": "Mustaqil tayyorgarlik uchun tuzilgan topshiriq va nazorat materiallari.",
            "count": independent_count,
            "count_label": "ta fayl",
            "category": "reading",
            "duration": "~4 soat",
            "difficulty": "Intermediate",
            "badge": "O'qish",
            "url_name": "independent",
            "icon": "book",
        },
        {
            "title": "Assignments",
            "description": "Amaliy topshiriqlar orqali mavzularni mustahkamlash uchun bo'lim.",
            "count": assignments_count,
            "count_label": "ta fayl",
            "category": "reading",
            "duration": "~2 soat",
            "difficulty": "Advanced",
            "badge": "Amaliyot",
            "url_name": "assignments",
            "icon": "assignment",
        },
        {
            "title": "Quiz Tests",
            "description": "Bilimingizni tekshirish va natijani darhol ko'rish uchun testlar.",
            "count": questions_count,
            "count_label": "ta savol",
            "category": "reading",
            "duration": "~1 soat",
            "difficulty": "Advanced",
            "badge": "Test",
            "url_name": "quiz",
            "icon": "quiz",
        },
    ]


def build_preview_url(file_field):
    if not file_field:
        return None

    return file_field.url

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
        'course_cards': build_course_cards(),
    }
    return render(request, 'home.html', context)


def presentations_list(request):
    presentations = PresentationsCategory.objects.all()
    for presentation in presentations:
        presentation.preview_url = build_preview_url(presentation.file)
    return render(request, 'presentations_list.html', {'presentations': presentations})


def casestudy_list(request):
    casestudies = CaseStudyCategory.objects.all()
    for casestudy in casestudies:
        casestudy.preview_url = build_preview_url(casestudy.file)
    return render(request, 'casestudy_list.html', {'casestudies': casestudies})


def listening_list(request):
    listenings = ListeningCategory.objects.all()
    return render(request, 'listening_list.html', {'listenings': listenings})


def independent_list(request):
    independents = IndependentWorkCategory.objects.all()
    for independent in independents:
        independent.preview_url = build_preview_url(independent.file)
    return render(request, 'independent_detail.html', {'independents': independents})


def assignments_list(request):
    assignments = AssignmentsCategory.objects.all()
    for assignment in assignments:
        assignment.preview_url = build_preview_url(assignment.file)
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
    return render(request, 'courses.html', {'course_cards': build_course_cards()})




