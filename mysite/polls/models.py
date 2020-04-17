from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class paperlist(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    project = models.IntegerField(default=0)
    status = models.DateTimeField('date published')
    actions = models.CharField(max_length=100)
