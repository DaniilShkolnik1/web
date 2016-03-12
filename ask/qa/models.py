from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    added_at = models.DateField(default=datetime.now(), blank=True)
    rating = models.IntegerField(11, default=0)
    author = models.CharField(max_length=30)
    likes = models.IntegerField(11, default=0)
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(default=datetime.now(), blank=True)
    author = models.CharField(max_length=30)
    question = models.ForeignKey('Question', null = True, on_delete=models.SET_NULL)
