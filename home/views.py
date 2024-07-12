from django.shortcuts import render
from .models import Room


# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'design with me'},
#     {'id':3, 'name':'Frontend develper'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'saleSawari/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'saleSawari/Room.html', context)
