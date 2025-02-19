from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model

# def registerUser(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect("home")
#     else:
#         form = RegisterForm ---> burada class vermelisen, moterizeleri qoymamisan.
#     context = {
#             "form" : form,
#         }
#     return render(request, "register.html", context)

def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    return render(request, "register.html", context)

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = get_user_model().objects.get(email=email)
        except:
            messages.error("user is not exist")
        user = authenticate(request, email=email, password=password)
            
        if user is not None:
            user.is_staff = True
            user.save()
            login(request, user) 
            return redirect("home")
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    context = {
        "form" : form
    }
    
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("home")


def listUsers(request):
    users = get_user_model().objects.all()
    paginator = Paginator(users, 2)  

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

    return render(request, "users.html", context)