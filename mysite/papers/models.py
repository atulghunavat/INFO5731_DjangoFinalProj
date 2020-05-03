# Create your models here.

from django.db import models

class Papers(models.Model):
    Paper_ID = models.AutoField(help_text="Paper ID:", primary_key=True)
    Paper_Title = models.CharField(max_length=250, help_text="Paper Title:")
    Paper_Description = models.CharField(max_length=280, help_text="Paper Description:")
    Paper_Content = models.BinaryField(max_length=None, help_text='Paper Content', default=0)
    """560 max length = 2x tweet character capacity"""
    Project_ID=models.ForeignKey('project.Project', db_column='Project_ID', on_delete=models.CASCADE, default= "")

    class Meta:
        db_table = 'Papers'