from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=120)

    def __repr__(self):
        return self.name
    

class Slip(models.Model):
    name = models.CharField(max_length=1000)

    def __repr__(self):
        return self.name