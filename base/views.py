from django.shortcuts import render

# Global rooms list
rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend development'},
]

# Create your views here.
def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == pk:
            room = i
    context = {'room': room}
    return render(request, 'base/rooms.html', context)