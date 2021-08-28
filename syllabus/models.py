from django.db import models

# Create your models here.
LEVEL_CHOICES = (
    ("jhs","Junior High Level"), ("shs","Senior High Level"), ("ig","International Exams")
    )
class Syllabus(models.Model):
    subject = models.CharField(max_length=200)
    course_levels = models.CharField(max_length=200, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=200)

    def __repr__(self):
        return self.title