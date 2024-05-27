from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Comment


# Create your views here.

def index(request, *args, **kwargs):
    post_id = request.GET.get('post_id', 7)
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/index.html', context)



def detail(request, *args, **kwargs):
    post_id = kwargs.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f'<h1>{post.title}</h1>'
                        f'<p>{post.content}</p>')


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f'<p>{comments.text}</p>')

