from django.db import models
from django.utils import timezone

# Create your models here.

class Elementlibrary(models.Model):
    elementid = models.AutoField(db_column='ElementID', primary_key=True)  
    elementname = models.CharField(db_column='ElementName', max_length=100)  
    described = models.CharField(db_column='Described', max_length=200, blank=True, null=True)  
    quizintro = models.CharField(db_column='QuizIntro', max_length=300, blank=True, null=True)  
    video = models.CharField(db_column='Video', max_length=200, blank=True, null=True)  
    picture = models.CharField(db_column='Picture', max_length=200, blank=True, null=True)  
    pdf = models.CharField(db_column='PDF', max_length=200, blank=True, null=True)  
    junctiontext = models.CharField(db_column='JunctionText', max_length=300, blank=True, null=True)  
    answer1 = models.CharField(db_column='Answer1', max_length=150, blank=True, null=True)  
    answer2 = models.CharField(db_column='Answer2', max_length=150, blank=True, null=True)  
    mainstream = models.BooleanField(db_column='Mainstream', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'ElementLibrary'






