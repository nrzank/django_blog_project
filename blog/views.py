from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Comment


# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'name': 'Nurzhan',
    }
    return render(request=request,
                  template_name='blog/index.html',
                  context=context
                  )




def detail(request, *args, **kwargs):
    post_id = request.objects.GET.get('post_id')
    post = Post.objects.get(Post, pk=post_id)

    return HttpResponse(f'<h1>{post.title}</h1>'
                        f'<p>{post.content}</p>')


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f'<p>{comments.text}</p>')
