from django.shortcuts import render
from clip.models import Window
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    context = {
            'windows' : Window.objects.all
            }
    return render(request, 'clip/index.html', context)

def submit(request):
    return HttpResponseRedirect(reverse('clip:result'))

def result(request):
    context = {
            }
    return render(request, "clip/result.html", context)
