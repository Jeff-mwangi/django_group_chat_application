
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room,Message

def home(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        username = request.POST['username']
        if  Room.objects.filter(room_name=room_name).exists():
            messages.info(request,'Room name already exists')
            return redirect('/'+room_name+'/?username='+username)
        else:
            room = Room.objects.create(room_name=room_name)
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('/'+room_name+'/?username='+username)
            else:
                user = User.objects.create(username=username)
                user.save()
                room.save()
                messages.success(request,'Room created successfully')
                return redirect('/'+room_name+'/?username='+username)
    else:
        return render(request,'home.html')

def send(request):
    text = request.POST['text']
    room_name = request.POST['room_name']
    username = request.POST['username']
    room = Room.objects.get(room_name=room_name)

    text = Message.objects.create(room_name=room,username=username,text=text)
    text.save()
    text.success(request,'Message sent successfully')


def room(request,room_name):
    username = request.GET.get('username')
    room = Room.objects.get(room_name=room_name)
    texts = Message.objects.filter(room_name=room)
    return render(request,'room.html',{'username':username,'room':room,'texts':texts})