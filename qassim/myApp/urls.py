from myApp import views
from django.urls import path
from .views import home, about, contact,unayzah,buraidah

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
    path('unayzah/',unayzah, name='unayzah'),
    path('buraidah/',buraidah,name='buraidah'),
    

    
]
