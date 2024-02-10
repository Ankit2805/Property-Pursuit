from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dealerapp import models
from dealerapp.models import property
from . import forms


def dashboard(request):
    total_properties = (
        property.objects.annotate(count=Count('id')).count()
    )
    total_dealers = (
        User.objects.filter(is_staff=True).filter(is_superuser=False).annotate(count=Count('id')).count()
    )
    total_buyers = (
        User.objects.filter(is_staff=False).annotate(count=Count('id')).count()
    )
    total_users = (
        User.objects.annotate(count=Count('id')).count()
    )
    print("userssssssssss",total_dealers)
    return render(request,'adminapp/index.html',{'total_properties':total_properties,
                                                 'total_dealers':total_dealers,
                                                 'total_buyers':total_buyers,
                                                 'total_users':total_users})

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

def property_manage_details_2(request):
    data = models.property.objects.all()
    photos = models.Image.objects.all()
    return render(request, 'adminapp/property-manage.html', {'P_E': data, 'photos': photos})


def showdetails_2(request, id):
    d = models.property.objects.get(id=id)
    photos = models.Image.objects.all()
    return render(request, 'adminapp/Show_Details.html', {'object': d, 'photos': photos})


def edit_property_2(request, id):
    a = models.property.objects.get(id=id)
    return render(request, 'adminapp/edit_property.html', {'object': a})


def update_property_2(request, id):
    a = models.property.objects.get(id=id)
    if request.method == "POST":
        updatesform = forms.updateform(request.POST, instance=a)
        if updatesform.is_valid():
            updatesform.save()
            print("akjndkjn", a)
            return redirect(property_manage_details_2)
        else:
            print(updatesform.errors)
            return HttpResponse("<h1>Error</h1>")
    else:
        return render(request, 'adminapp/edit_property.html', {'object': a})


def delete_property_2(request, id):
    models.property.objects.filter(id=id).delete()
    return redirect(property_manage_details_2)

def profile(request):
    return render(request, 'adminapp/users-profile.html')
