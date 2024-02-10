from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

def dashboard_0(request):
    return render(request,'client/index.html')

def login_0(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],
                                 password = request.POST['password'])
        if user is not None and  not user.is_staff and not user.is_superuser:
            auth.login(request,user)
            return redirect(dashboard_0)
        # elif user is not None and not user.is_superuser:
        # auth.login(request, user)
        #     return redirect(dashboard_0)
        else:
            return render(request, 'client/login.html', {'error': 'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request,'client/login.html')

def register_0(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])



                return render(request,'client/register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'))

                auth.login(request,user)
                return redirect(login_0)
        else:
                return render(request,'client/register.html',{'error':'password does not match'})

    else:
        return render(request,'client/register.html')

def logout(request):
    auth.logout(request)
    return redirect(register_0)