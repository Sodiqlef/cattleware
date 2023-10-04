from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


# Create your views here.


def blog_post_list(request):
    blog_posts = BlogPost.objects.order_by('-pub_date')
    return render(request, 'blog/blog_post_list.html', {'blog_posts': blog_posts})


def blog_post_detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    comments = Comment.objects.filter(post=blog_post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = blog_post
            comment.save()
            return redirect('blog_post_detail', post_id=blog_post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/blog_post_detail.html', {'blog_post': blog_post, 'comments': comments, 'form': form})


@login_required
def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_post_form.html', {'form': form})


def blog_post_edit(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', post_id=post_id)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/blog_post_form.html', {'form': form})
