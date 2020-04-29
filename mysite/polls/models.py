from django.db import models

# Create your models here.

from django.db import models


# class Question(models.Model):
# #     question_text = models.CharField(max_length=200)
# #     pub_date = models.DateTimeField('date published')
# #
# #
# # class Choice(models.Model):
# #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
# #     choice_text = models.CharField(max_length=200)
# #     votes = models.IntegerField(default=0)

class Project(models.Model):
    Project_ID = models.IntegerField(help_text="Project ID:", primary_key=True)
    Project_Title = models.CharField(max_length=50, help_text="Project Title:")
    Project_Description = models.CharField(max_length=560, help_text="Project Description:")
    # """560 max length = 2x tweet character capacity"""
    Project_Date = models.CharField(max_length=10, help_text="Date (mm/dd/yyyy):")

class Paper(models.Model):
    Paper_ID = models.IntegerField(help_text="Paper ID:", primary_key=True)
    Paper_Title = models.CharField(max_length=50, help_text="Paper Title:")
    Paper_Description = models.CharField(max_length=280, help_text="Paper Description:")
    Paper_Content = models.FileField(max_length=None, help_text='Paper Content', default=0)
    """560 max length = 2x tweet character capacity"""
    Project_ID=models.ForeignKey('Project', db_column='Project_ID', on_delete=models.CASCADE)