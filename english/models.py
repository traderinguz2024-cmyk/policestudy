from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Author(models.Model):
    first_name = models.CharField()
    second_name = models.CharField()

    def __str__(self):
        return self.first_name + " " + self.second_name

class PresentationsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField(resource_type="raw")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CaseStudyCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField(resource_type="raw")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ListeningCategory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    audio = models.FileField(
        upload_to='listening/',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.title


class IndependentWorkCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField(resource_type="raw")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AssignmentsCategory(models.Model):
    title = models.CharField(max_length=100)
    file = CloudinaryField(resource_type="raw")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

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

    def __str__(self):
        return self.text

from cloudinary_storage.storage import MediaCloudinaryStorage

class Document(models.Model):
    # Fayl maydoni
    file = models.FileField(storage=MediaCloudinaryStorage(), blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

