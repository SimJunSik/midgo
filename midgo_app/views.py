from django.shortcuts import render
from .models import *
# Create your views here.
def index(request) :

    user = User.objects.get(username = 'junsik')
    print(user.cats.all())

    return render(request, './index.html')