from django.shortcuts import render

from .models import Post


def post_list(request):

    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', data)
