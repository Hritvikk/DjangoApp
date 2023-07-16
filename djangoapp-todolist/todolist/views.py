from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'todolist/todolist_page.html', {'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.start_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'todolist/todolist_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'todolist/todolist_edit.html', {'form': form})

def post_completed(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_completed = not post.is_completed
    if post.end_date:
        post.end_date=None
    else:
        post.end_date = timezone.now()
    post.save()
    return HttpResponseRedirect('/')


def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect('/')