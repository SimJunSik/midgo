from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import *

# Create your views here.
def index(request) :

    return render(request, 'chat/index.html')

def room(request, room_name):

    user = request.user

    request.session['user_id'] = user.username

    chats = Chat.objects.filter(room_name = 'chat_' + room_name)
    context = { 'tests' : chats , 'room_name_json' : mark_safe(json.dumps(room_name)) , 'user' : user }

    return render(request, 'chat/room.html', context)