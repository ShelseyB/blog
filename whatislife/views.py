from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Comment
from django.template import loader


# Create your views here.
def index(request):
    latest_entry_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_entry_list': latest_entry_list}
    return render(request, 'whatislife/index.html', context)
    
def detail(request, entry_id):
    try:
        entry = Post.objects.get(pk=entry_id)
    except entry.DoesNotExist:
        raise Http404("Entry does not exist")
    return render(request, 'whatislife/detail.html', {'entry': entry})