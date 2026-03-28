from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

# PDF va Hujjatlar uchun umumiy qoida:
# resource_type='auto' va flags='attachment' (ixtiyoriy) yuklashni osonlashtiradi
class PresentationsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="materials/", max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CaseStudyCategory(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="materials/", max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class IndependentWorkCategory(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="materials/", max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class AssignmentsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="materials/", max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class ListeningCategory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    audio = models.FileField(upload_to="listening/", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Document(models.Model):
    file = models.FileField(upload_to="documents/", max_length=500, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
