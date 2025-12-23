from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PostForm
from .models import Post


def post_list(request):
    """Display all blog posts."""
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Display a single blog post."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    """Create a new blog post."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('blog:post_detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Post'})


def post_update(request, pk):
    """Update an existing blog post."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('blog:post_detail', args=[post.pk]))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Post', 'post': post})


def post_delete(request, pk):
    """Delete a blog post after confirmation."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('blog:post_list'))
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# Create your views here.
