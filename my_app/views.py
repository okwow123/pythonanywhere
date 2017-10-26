from django.utils import timezone
from my_app.models import Post
from django.shortcuts import render, get_object_or_404

def main(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'posts': posts})

def post_plus(request, pk):
    posts=Post.objects.get(no=pk)
    posts.good_count=posts.good_count+1
    Post.objects.filter(no=pk).update(good_count=posts.good_count)
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'posts': posts})

