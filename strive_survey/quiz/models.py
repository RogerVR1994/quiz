from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    question_id = models.IntegerField()
    
class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_id = models.IntegerField()

class Quiz(models.Model):
    title = models.CharField(max_length=500)
    quiz_id = models.IntegerField()

class Results(models.Model):
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()