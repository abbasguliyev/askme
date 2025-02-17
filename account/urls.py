from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.registerUser, name="register"),
    path('users/', views.registerUser, name="users"),
]
