from django.shortcuts import render , HttpResponse,redirect
from dealerapp import models
from clientapp import forms
from django.contrib import auth
from django.contrib.auth.models import User
from clientapp.models import bookingrequest
from dealerapp.models import Image
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_0(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None and not user.is_staff and not user.is_superuser:
            auth.login(request, user)
            return redirect(index)
        else:
            return render(request, 'client/login.html',{'error': 'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request, 'client/login.html')
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

@login_required(login_url='login_0')
def index(request):
    data = models.property.objects.all()
    photos = models.Image.objects.all()
    context = {'data': data,'photos':photos}
    return render(request,'client/index.html',context=context)

@login_required(login_url='login_0')
def property_details(request,id):
    pd = models.property.objects.get(id=id)
    photos = models.Image.objects.all()
    return render(request, 'client/property-details.html',{'o':pd, 'photos':photos})

@login_required(login_url='login_0')
def sendrequest(request,id):
    pd = models.property.objects.get(id=id)
    print(pd)
    form = bookingrequest()
    if request.method == "POST":
        print("helooooooooooooooo")
        form.user=request.user
        print(form.user)
        form.prop=pd
        print(form.prop)
        form.save()
        print("objects",form)
        return redirect(index)
        # else:
        #     print(form.errors)
    return render(request,'client/property-details.html')

@login_required(login_url='login_0')
def properties(request):
    return render(request,'client/properties.html')

@login_required(login_url='login_0')
def buy(request):
    return render(request,'client/buy.html')

@login_required(login_url='login_0')
def view_list(request):
    return render(request,'client/view-list.html')

@login_required(login_url='login_0')
def about(request):
    return render(request,'client/about.html')

@login_required(login_url='login_0')
def contact(request):
    return render(request,'client/contact.html')

@login_required(login_url='login_0')
def profile(request):
    return render(request,'client/users-profile.html')

def logout(request):
    auth.logout(request)
    return redirect(register_0)