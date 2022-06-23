from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Room

# rooms = [
#     {'id':1, 'name':'Learn Python'},
#     {'id':2, 'name':'Learn Java'},
#     {'id':3, 'name':"Let's designn"},

# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):   
    room = Room.objects.get(id=pk)

    context = {'room': room}      
    return render(request, 'base/room.html', context)
