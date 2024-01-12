from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def dashboard(request):
    return render(request,'adminapp/index.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],
                                 password = request.POST['password'])
        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect(dashboard)
        else:
            return render(request, 'adminapp/login.html', {'error': 'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request,'adminapp/login.html')

def register(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])



                return render(request,'adminapp/register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'))

                auth.login(request,user)
                return redirect(login)
        else:
                return render(request,'adminapp/register.html',{'error':'password does not match'})

    else:
        return render(request,'adminapp/register.html')
