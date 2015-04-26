from django.shortcuts import render

#   def index(request):
              place_holder = 'To be replaced'
              context = {'place_holder': place_holder}
              return render(request, 'friendsapp/index.html', context)
