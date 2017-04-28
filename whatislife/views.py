from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Post, Comment
from django.template import loader
from django.core.urlresolvers import reverse
import time
from django.db import models
from datetime import datetime


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
    
def new_comment(request, entry_id):
    post = get_object_or_404(Post, pk=entry_id)
    # try:
    #     pk=request.POST['comment_author']
    #     selected_choice = post.comment_set.get(pk)
    # except (KeyError, Comment.DoesNotExist):
    #     return render(request, 'whatislife/detail.html', {
    #         'post': post,
    #         'error_message': "You didn't fill out the form."
    #     })
    
    comment = Comment.objects.create_comment(post, request.POST['comment_entry'], request.POST['comment_author'])
    #comment = cls (post=post, comment_entry=comment_entry, pub_date=pub_date, comment_author=comment_author)
    comment.save()
    #return render(request, "whatislife/detail.html")
    #return HttpResponseRedirect(reverse('whatislife:detail', args=(post.id)))
    return HttpResponseRedirect(reverse('whatislife:index'))
    