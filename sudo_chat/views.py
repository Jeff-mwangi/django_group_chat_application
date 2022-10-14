
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Room,Message
from django.http import HttpResponse, JsonResponse

def home(request):
    rooms = Room.objects.all()

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
        return render(request,'home.html',{'rooms':rooms})

def room(request,room_name):
    username = request.GET.get('username')
    # solve error Room matching query does not exist.
    if Room.objects.filter(room_name=room_name).exists():
        room = Room.objects.get(room_name=room_name)
        texts = Message.objects.filter(room_name=room)
        # get all the usernames in the room
        users = []
        for text in texts:
            users.append(text.username)
        # remove duplicates
        users = list(dict.fromkeys(users))
        return render(request,'room.html',{'room':room,'username':username,'texts':texts,'users':users})
    else:
        return redirect('/')
    
def send(request,room_name):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        username = request.POST['username']
        text = request.POST['text']
        print(room_name,username,text)
        room = Room.objects.get(room_name=room_name)
        message = Message.objects.create(room_name=room,username=username,text=text)
        message.save()
        return HttpResponse('Message sent successfully')
    else:
        return HttpResponse('Request method is not a POST')

def get_messages(request,room_name):
    if request.method == 'GET':
        room = Room.objects.get(room_name=room_name)
        texts = Message.objects.filter(room_name=room)
        return JsonResponse({'texts':list(texts.values())})
    else:
        return HttpResponse('Request method is not a GET')

def get_count(request,room_name):
    if request.method == 'GET':
        room = Room.objects.get(room_name=room_name)
        texts = Message.objects.filter(room_name=room)
        return JsonResponse({'count':texts.count()})
    else:
        return HttpResponse('Request method is not a GET')

