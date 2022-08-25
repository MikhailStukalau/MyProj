from django.shortcuts import render
from .models import Comment


# Create your views here.
def blog_index(request):
    comments = Comment.objects.all().order_by('created_on')
    context = {
        'comments': comments
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, id):
    comment = Comment.objects.get(id=id)
    context = {
        'comment': comment
    }
    return render(request, 'blog_detail.html', context)
