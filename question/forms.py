from django import forms
from .models import Tag, Question, Answer

class TagForms(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name",]

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'description']