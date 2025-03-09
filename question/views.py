from django.shortcuts import render, redirect
from .models import Question, Answer, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .forms import QuestionForm, AnswerForm

def listQuestions(request,):
    question = Question.objects.all()
    paginator = Paginator(question, 10)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "page_obj" : page_obj,
    }
    return render(request, "question.html", context)



def detailQuestion(request,pk):
    questions = Question.objects.get(pk=pk)
    get_answer = Answer.objects.filter(question=questions)
    get_tag = Tag.objects.filter(tag__pk=pk)
    context = {
        "question" : questions,
        "answer" : get_answer,
        "tag" : get_tag,
    }
    return render(request,'detail.html',context)

def AddQuestions(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()
            return redirect('questions')
    else:
        form = QuestionForm()

        context = {
            "form" : form,
        }
    return render(request,'add_questions.html', context)

def AddAnswers(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('detail', pk=pk)
    else:
        form = AnswerForm()
        context = {
            "form" : form,
        }
    return render(request,'add_answers.html', context)

def listTags(request):
    tags = Tag.objects.all()
    context = {
        "tags" : tags,
    }
    return render(request, 'tags.html', context)

def question_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        questions = Question.objects.filter(title__contains=searched)
        context = {
        "searched" : searched,
        "questions" : questions,
        }
        return render(request, "filter_question.html", context)
    else:
        context = {
        }
        return render(request, "filter_question.html", context)
    
def delete_questions(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    return redirect('questions')

def detailTag(request,pk):
    tag = get_object_or_404(Tag, pk=pk)
    question = Question.objects.filter(tag=tag)    
    context = {
        "tag" : tag,
        "question" : question,
    }
    return render(request,'filter_tag.html',context)
    
