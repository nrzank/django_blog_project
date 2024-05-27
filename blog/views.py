from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post, Comment


# Create your views here.


def post_get(request, *args, **kwargs):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    print(kwargs.GET)
    print(post)
    return HttpResponse(f'<h1>{post.title}</h1>'
                        f'<p>{post.content}</p>')



def detail(request, *args, **kwargs):
    post_id = kwargs.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f'<h1>{post.title}</h1>'
                        f'<p>{post.content}</p>')


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f'<p>{comments.text}</p>')

