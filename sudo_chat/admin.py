from django.contrib import admin
from .models import Room,Message
from django.contrib.auth.models import User

admin.site.register(Room)
admin.site.register(Message)