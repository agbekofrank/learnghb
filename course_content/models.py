from django.db import models

# Create your models here.
LEVEL_CHOICES = (
    ("jhs","Junior High Level"), ("shs","Senior High Level"), ("ig","International Exams")
    )

class Subject(models.Model):
    title = models.CharField(max_length=200)

class Syllabus(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_levels = models.CharField(max_length=200, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=200)

    def __repr__(self):
        return self.title
