from django.urls import path, include
from . import views
from django_filters.views import FilterView
from .models import Question
urlpatterns = [
    path("detail/<int:pk>", views.detailQuestion, name="detail"),
    path("detail_tag/<int:pk>", views.detailTag, name="detail_tag"),
    path("delete/<int:pk>", views.delete_questions, name="delete"),
    path("questions", views.listQuestions, name="questions"),
    path("Tags", views.listTags, name="tags"),
    path("add_questions", views.AddQuestions, name="add_questions"),
    path("add_answers/<int:pk>", views.AddAnswers, name="add_answers"),
    path("search", views.question_search, name="search"),
]
