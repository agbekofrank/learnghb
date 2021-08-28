from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post
from  .forms import PostForm
# Create your views here.

@login_required(login_url='accounts:login')
def posts_create(req):
    form = PostForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(req, "Successfully created " + instance.title)
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Create',
        'form': form,
    }
    # print('|||||' * 10)
    return render(req, 'post_form.html', context)


def posts_list(req):
    posts = Post.objects.active()
    paginator = Paginator(posts, 3) # Show 25 contacts per page.
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # search query
    query = req.GET.get('q')
    if query:
        page_obj = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__username__icontains=query) 
            ).distinct()
    context = {
        'title': 'Posts Home',
        'posts': posts,
        'page_obj': page_obj
    }
    return render(req, 'posts_list.html', context)

def post_detail(req, slug=None):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(req, 'post_detail.html', context)

@login_required(login_url='accounts:login')
def posts_update(req, slug=None):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(req.POST or None, req.FILES or None, instance=post)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        return HttpResponseRedirect(inst.get_absolute_url())
    context = {
        'title': 'Update',
        'inst': post,
        'form': form
    }
    return render(req, 'post_form.html', context)


def posts_delete(req, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(req, "Successfully deleted ")
    return redirect('posts:list')
