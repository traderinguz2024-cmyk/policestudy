from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import MediaCloudinaryStorage

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

# PDF va Hujjatlar uchun umumiy qoida:
# resource_type='auto' va flags='attachment' (ixtiyoriy) yuklashni osonlashtiradi
class PresentationsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField('file', resource_type="auto", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CaseStudyCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField('file', resource_type="auto", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class IndependentWorkCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField('file', resource_type="auto", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class AssignmentsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField('file', resource_type="auto", blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class ListeningCategory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Audio uchun resource_type="video" Cloudinary-da audio/video uchun standart hisoblanadi
    # Agar "auto" xato bersa, "video" deb yozish ham yechim bo'ladi
    audio = CloudinaryField('audio', resource_type="auto", blank=True, null=True)

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
    # Bu yerda storage ishlatsangiz, settings.py dagi sozlamalar bilan mos tushishi kerak
    file = models.FileField(storage=MediaCloudinaryStorage(), blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)