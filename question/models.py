from django.db import models


class Question(models.Model):
    question = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

class Answer(models.Model):
    answer = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)