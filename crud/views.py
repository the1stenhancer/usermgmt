from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, DetailForm
from .models import Detail

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
