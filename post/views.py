from typing import List
from django.http.response import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django import http
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView

from .models import *
from .forms import PostComment, PostForm

# Create your views here.
def posts(request):
    if request.user.is_authenticated:
        categorys = Categorys.objects.all()
        posts = Post.objects.all()

        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(name__icontains = search)
            return render(request, 'post/query.html', {'posts': posts})

        return render(request, 'post/index.html', {'categorys': categorys})
    messages.error(request, 'You cant access.')
    return HttpResponseRedirect('/')

def profile(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(name__icontains = search)
            return render(request, 'post/query.html', {'posts': posts})

        return render(request, 'post/profile.html')
    messages.error(request, 'Join to access the page.')
    return HttpResponseRedirect('/')

def add_post(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(name__icontains = search)
            return render(request, 'post/query.html', {'posts': posts})
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                post = Post.objects.filter(name=request.POST['name']).update(user=request.user.id)
                messages.info(request, 'Post added succesfully.')
                return HttpResponseRedirect('/main')
            else:
                messages.error(request, 'Error, invalid fields.')
                form = PostForm()
                # return render(request, 'post/add_post.html', {'form': form})
        else:
            form = PostForm()
        return render(request, 'post/add_post.html', {'form': form})
    messages.error(request, 'You cant access.')
    return HttpResponseRedirect('/')

class CategoryDetailView(DetailView):
    model = Categorys

def PostView(request, id):
    form = PostComment()
    if request.user.is_authenticated:
        posts = Post.objects.all()

        search = request.GET.get('search')
        if search:
            posts = Post.objects.filter(name__icontains = search)
            return render(request, 'post/query.html', {'posts': posts})
        post = get_object_or_404(Post, pk=id)
        if request.method=='POST':
            print(request.POST['comment'])
            if form.is_valid:
                user = get_object_or_404(User, id=request.user.id)
                post_instance = get_object_or_404(Post, id=id)
                comment = Comment(text=request.POST['comment'])
                comment.user = user
                comment.post = post_instance
                comment.save()
                messages.info(request, 'Comment added with success.')
                return render(request, 'post/post_detail.html', {'post': post, 'form': form})
            form = PostComment()
            messages.error(request, 'Invalid data.')
        form = PostComment()
        return render(request, 'post/post_detail.html', {'post': post ,'form': form})
    # return render(request, 'post/post_detail.html', {'post': post})
    return HttpResponseRedirect('/')

def PostDelete(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.user.id == request.user.id:
        post.delete()
        messages.info(request, 'Post deleted with success.')
        return HttpResponseRedirect('/')
    messages.error(request, 'You dont have permission to delete this post.')
    return HttpResponseRedirect('/')

def CommentDelete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if comment.user.id == request.user.id:
        comment.delete()
        messages.info(request, 'Comment deleted with success.')
        return HttpResponseRedirect('/')
    messages.error(request, 'You dont have permission to delete this comment.')
    return HttpResponseRedirect('/')