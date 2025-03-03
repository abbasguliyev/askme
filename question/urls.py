from django.urls import path, include
from . import views

urlpatterns = [
    path("detail/<int:pk>", views.detailQuestion, name="detail"),
    path("", views.listQuestions, name="question"),
]
