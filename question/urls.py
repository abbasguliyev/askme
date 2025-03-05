from django.urls import path, include
from . import views

urlpatterns = [
    path("detail/<int:pk>", views.detailQuestion, name="detail"),
    path("questions", views.listQuestions, name="questions"),
    path("Tags", views.listTags, name="tags"),
    path("add_questions", views.AddQuestions, name="add_questions"),
    path("add_answers/<int:pk>", views.AddAnswers, name="add_answers"),
]
