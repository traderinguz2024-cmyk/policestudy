from rest_framework import serializers
from english.models import *
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationsCategory
        fields = '__all__'

class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudyCategory
        fields = '__all__'

class ListeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningCategory
        fields = '__all__'

class IndependentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndependentWorkCategory
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentsCategory

        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


