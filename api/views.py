from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import random

@api_view(['GET'])
def all_categories(request):
    data = {
        "presentations": PresentationSerializer(PresentationsCategory.objects.all(), many=True).data,
        "case_studies": CaseStudySerializer(CaseStudyCategory.objects.all(), many=True).data,
        "listenings": ListeningSerializer(ListeningCategory.objects.all(), many=True).data,
        "independent_works": IndependentSerializer(IndependentWorkCategory.objects.all(), many=True).data,
        "assignments": AssignmentSerializer(AssignmentsCategory.objects.all(), many=True).data,
    }
    return Response(data)

@api_view(['GET'])
def category_detail(request, type, pk):

    model_map = {
        "presentation": PresentationsCategory,
        "case": CaseStudyCategory,
        "listening": ListeningCategory,
        "independent": IndependentWorkCategory,
        "assignment": AssignmentsCategory,
    }

    model = model_map.get(type)

    if not model:
        return Response({"error": "Wrong category type"}, status=400)

    obj = model.objects.get(pk=pk)

    serializer_map = {
        PresentationsCategory: PresentationSerializer,
        CaseStudyCategory: CaseStudySerializer,
        ListeningCategory: ListeningSerializer,
        IndependentWorkCategory: IndependentSerializer,
        AssignmentsCategory: AssignmentSerializer,
    }

    serializer = serializer_map[model](obj)

    return Response(serializer.data)

@api_view(['GET'])
def start_test(request):

    # Barcha savollarni olish
    questions = list(Question.objects.all())

    # Random aralashtirish
    random.shuffle(questions)

    # Faqat 15 tasi
    questions = questions[:15]

    data = []

    for q in questions:
        data.append({
            "id": q.id,
            "text": q.text,
            "choices": ChoiceSerializer(q.choices.all(), many=True).data
        })

    return Response(data)
@api_view(['POST'])
def check_test(request):

    answers = request.data.get("answers", {})
    correct = 0
    total = len(answers)

    for question_id, choice_id in answers.items():
        try:
            choice = Choice.objects.get(id=choice_id)
            if choice.is_correct:
                correct += 1
        except:
            pass

    return Response({
        "correct": correct,
        "total": total,
        "score": round((correct/total)*100, 2) if total else 0
    })
