from django.shortcuts import render
from .models import Comment, Post


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    comment = Comment.objects.GET(id=pk)
    context = {
        'comment': comment
    }
    return render(request, 'blog_detail.html', context)
