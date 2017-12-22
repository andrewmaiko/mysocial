from django.shortcuts import render
from friendapp.models import User, Comment
import os.path

def index(request):
            # myuser = User.objects.filter(id=2)
             plots = [('friendapp/' + plot) for plot in os.listdir('C:/django/mysocial/friendapp/static/friendapp') if os.path.isfile(os.path.join('C:/django/mysocial/friendapp/static/friendapp',plot))]
             context = {'plots': plots}
             return render(request, 'friendapp/index.html', context)
