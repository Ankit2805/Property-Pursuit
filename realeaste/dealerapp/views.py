from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from . import forms
from clientapp.models import bookingrequest
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_1(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],
                                 password = request.POST['password'])
        if user is not None and user.is_staff:
            auth.login(request,user)
            return redirect(dashboard_1)
        else:
            return render(request, 'dealer/NEWLOGIN.html', {'error':'Invalid Username Or Password pls try again or complete the Registration'})
    else:
        return render(request,'dealer/NEWLOGIN.html')

def register_1(request):
    if request.method == "POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'dealer/newreg.html',{'error':'username is already exist'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password1'),
                                                is_staff = True)
                auth.login(request,user)
                return redirect(login_1)
        else:
                return render(request,'dealer/newreg.html',{'error':'password does not match'})

    else:
        return render(request,'dealer/newreg.html')

@login_required(login_url='login_1')
def dashboard_1(request):
    return render(request,'dealer/index.html')

@login_required(login_url='login_1')
def property_add_details(request):
    if request.method == "POST":
        detailform = forms.detailsform(request.POST,request.FILES)
        if detailform.is_valid():
            object = detailform.save(commit=False)
            object.user=request.user
            object.save()

            photos = request.FILES.getlist('p_image')
            for image in photos:
                img = models.Image.objects.create(p_image=image,
                                                  proty=object)
                print("photo added")
            return redirect(property_manage_details)
        else:
            print(detailform.errors)
            return render(request,'dealer/property-add_details.html',{'error':'Pls fill out all the details.'})
    else:
     return render(request, 'dealer/property-add_details.html')

@login_required(login_url='login_1')
def property_manage_details(request):
        data = models.property.objects.filter(user_id=request.user).prefetch_related('image_set')
        # photos = models.Image.objects.all()
        return render(request, 'dealer/property-manage.html', {'P_E': data})

@login_required(login_url='login_1')
def showdetails(request,id):
   d = models.property.objects.get(id=id)
   photos = models.Image.objects.all()
   return render(request, 'dealer/Show_Details.html',{'object':d,'photos': photos})

@login_required(login_url='login_1')
def edit_property(request,id):
    a=models.property.objects.get(id=id)
    return render(request,'dealer/edit_property.html',{'object':a})

@login_required(login_url='login_1')
def update_property(request,id):
    a = models.property.objects.get(id=id)
    b = models.Image.objects.filter(proty_id=id)
    if request.method == "POST":
        updatesform = forms.updateform(request.POST, instance=a)
        photos = request.FILES.getlist('p_image')
        print(photos)
        if updatesform.is_valid():
            obj = updatesform.save(commit=False)
            obj.save()
            b.delete()
            print("helooooooooooooo")
            for img in photos:
                print("hhhhhhhhhhhh")
                photo = models.Image.objects.create(p_image=img,proty=obj)
                print("loop added")
            print("heloiiiiiiiiiiiiiiiiiiii")

            print("akjndkjn",a)
            return redirect(property_manage_details)
        else:
            print(updatesform.errors)
            return render(request,'dealer/edit_property.html',{'error':'Pls fill out all the details.'})
    else:
        return render(request, 'dealer/edit_property.html',{'object':a})

@login_required(login_url='login_1')
def delete_property(request,id):
    models.property.objects.filter(id=id).delete()
    return redirect(property_manage_details)

def logout(request):
    auth.logout(request)
    return redirect(register_1)

@login_required(login_url='login_1')
def booking_history(request):
    br = bookingrequest.objects.filter(user_id=request.user)
    return render(request, 'dealer/Booking_history.html', {'br': br})

def delete_booking(request,id):
    bookingrequest.objects.filter(id=id).delete()
    return redirect(booking_history)

@login_required(login_url='login_1')
def feedback(request):
    if request.method == "POST":
        feedbackform = forms.Feedback(request.POST)
        if feedbackform.is_valid():
            feedbackform.save()
            return redirect(dashboard_1)
        else:
            return render(request,'dealer/contact.html',{'error':'Pls fill out all the details.'})
    return render(request,'dealer/contact.html')

@login_required(login_url='login_1')
def profile(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        new_email = request.POST.get('new_email')
        if new_username or new_email:
            user = request.user
            user.username = new_username
            user.email = new_email
            user.save()
            return redirect('profile')  # Redirect to the profile page after updating the username
        else:
            # Handle the case where the form is not valid or the username is empty
            return render(request, 'dealer/users-profile.html', {'error': 'Invalid form or empty Username or Email'})
    return render(request,'dealer/users-profile.html')
