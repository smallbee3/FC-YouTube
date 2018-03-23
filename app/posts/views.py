from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import CommentForm
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', data)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all()
    comment_form = CommentForm()
    data = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'post/post_detail.html', data)


def comment_create(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        # content = request.get('content')
        #
        # if not content:
        #     return HttpResponse('댓글내용을 입력하세요.', status=400)
        #
        # Comment.objects.create(
        #     author=request.user,
        #     post=post,
        #     content=content,
        # )
        # return redirect()

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            messages.success(request, '댓글이 등록되었습니다')
        else:
            error_msg = '댓글 등록에 실패했습니다\n{}'.format(
                '\n'.join(
                    [f'- {error}'
                     for key, value in comment_form.errors.items()
                     for error in value]))
            messages.error(request, error_msg)

        return redirect('post:post-detail', pk=pk)
