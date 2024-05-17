from django.contrib import admin
from .models import Message
from .models import Place
#user:haya
#pessword 12345
admin.site.register(Place)

admin.site.register(Message)
