from django.shortcuts import render

# Create your views here.
def home(request):
    rooms = [
        {'id': 1, 'name': 'Lets learn python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend development'},
    ]
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    return render(request, 'rooms.html')


def rooms(request, pk):
    return render(request, 'base/rooms.html')


