from django.db import models
from account.models import get_user_model   
    


class Tag(models.Model):
    name = models.TextField(max_length=30)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    title = models.TextField(max_length=90)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='tag')

    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    answer = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.answer