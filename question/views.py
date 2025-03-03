from django.shortcuts import render, redirect
from .models import Question, Answer, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

def listQuestions(request):
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