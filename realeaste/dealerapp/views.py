from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import forms
# Create your views here.

def login_1(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],
                                 password = request.POST['password'])
        if user is not None and user.is_staff:
            auth.login(request,user)
            return redirect(dashboard_1)
        else:
            return render(request, 'dealer/login.html', {'error':'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request,'dealer/login.html')

def register_1(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'dealer/register.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'),
                                                is_staff = True)
                auth.login(request,user)
                return redirect(login_1)
        else:
                return render(request,'dealer/register.html',{'error':'password does not match'})

    else:
        return render(request,'dealer/register.html')



def dashboard_1(request):
    return render(request,'dealer/index.html')

def property_add_details(request):
    if request.method == "POST":
        detailform = forms.detailsform(request.POST,request.FILES)
        if detailform.is_valid():
            object = detailform.save(commit=False)
            object.save()
            photos = request.FILES.getlist('p_image')
            for image in photos:
                imge = str(image)
                img = models.Image.objects.create(p_image=imge,
                                                  proty=object)
                print("photo added")
            return redirect(dashboard_1)
        else:
            print(detailform.errors)
            return HttpResponse("<h1>Error</h1>")
    return render(request, 'dealer/property-add_details.html')

def property_manage_details(request):
        data = models.property.objects.all()
        photos = models.Image.objects.all()
        return render(request, 'dealer/property-manage.html', {'P_E': data,'photos': photos})

def showdetails(request,id):
   d = models.property.objects.get(id=id)
   i = models.Image.objects.filter(id=id)
   return render(request, 'dealer/Show_Details.html',{'object':d})

def edit_property(request,id):
    a=models.property.objects.get(id=id)
    return render(request,'dealer/edit_property.html',{'object':a})

def update_property(request,id):
    a = models.property.objects.get(id=id)
    if request.method == "POST":
        updatesform = forms.updateform(request.POST, instance=a)
        if updatesform.is_valid():
            updatesform.save()
            print("akjndkjn",a)
            return redirect(property_manage_details)
        else:
            print(updatesform.errors)
            return HttpResponse("<h1>Error</h1>")
    else:
        return render(request, 'dealer/edit_property.html',{'object':a})

def delete_property(request,id):
    models.property.objects.filter(id=id).delete()
    return redirect(property_manage_details)

def logout(request):
    auth.logout(request)
    return redirect(register_1)
def booking_history(request):
    return render(request,'dealer/Booking_history.html')

def contact(request):
    return render(request,'dealer/contact.html')

def profile(request):
    return render(request,'dealer/users-profile.html')
