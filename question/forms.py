from django import forms
from .models import Tag, Question, Answer

class TagForms(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name",]

class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class" : "form-control"}
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={"class" : "form-control"}
    ))
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple(
        attrs={}
    ))
      
    class Meta:
        model = Question
        fields = ['title', 'description', 'tag']
        
class AnswerForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea(
        attrs={"class" : "form-control"}
    ))
    
    class Meta:
        model = Answer
        fields = ['answer',]
            
