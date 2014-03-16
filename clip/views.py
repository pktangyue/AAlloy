from django.shortcuts import render
from clip.models import Window
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def index(request):
    context = {
            'windows' : Window.objects.all
            }
    return render(request, 'clip/index.html', context)

def result(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("clip/result.html", c)
