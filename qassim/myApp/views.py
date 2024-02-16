from django.shortcuts import render,redirect
from myApp import views

def home(request):
    return render(request,"myApp/home.html")
