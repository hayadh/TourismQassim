from django.shortcuts import render,redirect
from myApp import views


def home(request):
    return render(request, "myApp/home.html")

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request, 'myApp/contact.html')
def unayzah(request):
    return render(request, 'myApp/unayzah.html')


