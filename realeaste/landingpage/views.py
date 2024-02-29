from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
def landing(request):
    return render(request,'landing/landing.html')