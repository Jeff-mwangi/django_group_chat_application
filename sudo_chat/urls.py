from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room_name>/',views.room,name='room'),
    path('send/',views.send,name='send'),
]
