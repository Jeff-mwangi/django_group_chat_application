from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room_name>/',views.room,name='room'),
    path('<str:room_name>/send/',views.send,name='send'),
    # get messsages from the room
    path('get_messages/<str:room_name>/',views.get_messages,name='get_messages'),
    path('get_count/<str:room_name>/',views.get_count,name='get_count'),
]
