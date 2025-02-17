from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate


def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("home")
    else:
        form = RegisterForm
    context = {
            "form" : form,
        }
    return render(request, "register.html", context)

def login(request):
    ...