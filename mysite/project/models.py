from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    Project_ID = models.AutoField(help_text="Project ID:", primary_key=True)
    Project_Title = models.CharField(max_length=250, help_text="Project Title:")
    Project_Description = models.CharField(max_length=560, help_text="Project Description:")
    # """560 max length = 2x tweet character capacity"""
    Project_Date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'Project'