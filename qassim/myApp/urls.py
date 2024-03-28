from myApp import views
from django.urls import path
from .views import home, about, contact,unayzah

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
    path('unayzah/',unayzah, name='unayzah'),
    

    
]
