from django.shortcuts import render
from friendapp.models import User, Comment

def index(request):
             myuser = User.objects.filter(id=2)
             context = {'myuser': myuser}
             return render(request, 'friendapp/index.html', context)
