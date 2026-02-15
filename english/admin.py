from django.contrib import admin
from .models import *

# Register your models
admin.site.register(PresentationsCategory)
admin.site.register(CaseStudyCategory)
admin.site.register(ListeningCategory)
admin.site.register(IndependentWorkCategory)
admin.site.register(AssignmentsCategory)
admin.site.register(Author)
from django.contrib import admin
from django import forms
from .models import Question, Choice

# Inline class
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # default 4 variant chiqadi
    min_num = 2
    max_num = 4
    fields = ('text', 'is_correct')
    # Radio tugma uchun Boolean o‘rniga Select qilish mumkin, lekin oddiy holatda checkbox ishlatamiz

# Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    def save_formset(self, request, form, formset, change):
        """
        Shu yerda to'g'ri javob bitta ekanligini tekshirish mumkin
        """
        instances = formset.save(commit=False)
        correct_count = sum(1 for obj in instances if obj.is_correct)
        if correct_count != 1:
            raise forms.ValidationError("Har bir savolga faqat bitta to'g'ri javob bo'lishi kerak!")
        for obj in instances:
            obj.save()
        formset.save_m2m()

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

