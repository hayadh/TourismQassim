from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact
from .models import Message

def home(request):
    return render(request, "myApp/home.html")

def about(request):
    return render(request, 'myApp/about.html')

def contact(request):
    return render(request,'myApp/contact.html')
def unayzah(request):
    return render(request,'myApp/unayzah.html')
def buraidah(request):
    return render(request,'myApp/buraidah.html')






def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')  

        
        msg_instance = Message.objects.create(name=name, email=email, message=message)

        
        messages.success(request, 'Message sent successfully!')

        
        return redirect('contact')  
    
    
    return render(request, 'myApp/contact.html')


