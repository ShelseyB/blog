from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Blog homepage")
    
def detail(request, entry_title):
    return HttpResponse("You're looking at %s." % entry_title)