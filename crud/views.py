from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, DetailForm, LoginForm

# Create your views here.

def dashboard(request):
    return render(
        request=request, 
        template_name='main/dashboard.html',
        context={}
    )


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        detail_form = DetailForm(data=request.POST)
        if user_form.is_valid() and detail_form.is_valid():
            new_user = user_form.save()
            new_user_detail = detail_form.save(commit=False)
            new_user_detail.user = new_user
            new_user_detail.save()
            return redirect("crud:dashboard")
    else:
        user_form = UserForm()
        detail_form = DetailForm()
    
    return render(
        request=request,
        template_name="main/register.html",
        context={
            "uform": user_form,
            "dform": detail_form,
        }
    )


def login_view(request, next):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd["username"]
            password = cd["password"]
            user = authenticate(
                reuqest=request,
                credentials={
                    "username": username,
                    "password": password
                }
            )
            if user is not None:
                login(request=request, user=user)
                return redirect(f"crud:{next}")
    else:
        form = LoginForm()
    
    return render(
        request=request,
        template_name="main/login.html",
        context={
            "form": form
        }
    )


def logout_view(request):
    if request.user.is_authenticated:
        logout(request=request)
    return redirect("crud:dashboard")
