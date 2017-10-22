from django.shortcuts import render
from django.utils import timezone
from my_app.models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
