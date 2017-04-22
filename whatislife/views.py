from django.shortcuts import render, get_object_or_404
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
    
def new_comment(request, entry_id):
    post = get_object_or_404(Post, pk=entry_id)
    try:
        selected_choice = post.comment_set.get(pk=request.POST['choice'])
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'whatislife/detail.html', {
            'post': post,
            'error_message': "You didn't fill out the form.",
        })
    selected_choice.new_comment(selected_choice, selected_choice.post, selected_choice.comment_entry, selected_choice.pub_date, selected_choice.comment_author)
    selected_choice.save()
    return render(request, 'whatislife/detail.html', {'entry': post})
    