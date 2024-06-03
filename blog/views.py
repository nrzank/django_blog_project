from django import views
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import CommentModelForms, PostModelForms
from blog.models import Post, Comment


# Create your views here.

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request=request,
                  template_name='blog/index.html',
                  context=context
                  )


class PostView(views.View):


    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts': posts,
        }
        return render(request=request,
                      template_name='blog/index.html',
                      context=context
                      )


def create_post(request, *args, **kwargs):
    print(f'Метод запроса: {request.method}')

    if request.method == 'GET':
        return render(request=request,
                      template_name='blog/create_post.html',
                      )


    elif request.method == 'POST':

        form = PostModelForms(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)

            new_post.author_id = 1

            new_post.save()

            return HttpResponse(f'<h1> Комментарии создан! </h1>'

                                f'<h2>{new_post.pk}: {new_post.post}</h2>'

                                f'<h2>{new_post.text}</h2>')

    return HttpResponse(f'<h1>Метод не разрешен</h1>')


def create_comment(request, *args, **kwargs):
    print(f'Метод запроса: {request.method}')

    if request.method == 'GET':
        context = {
            'my_form': CommentModelForms(),
        }
        return render(request=request,
                      template_name='blog/create_comment1.html',
                      context=context
                      )

    elif request.method == 'POST':
        form = CommentModelForms(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author_id = 1
            new_comment.save()
            return HttpResponse(f'<h1> Комментарии создан! </h1>'
                                f'<h2>{new_comment.pk}: {new_comment.post}</h2>'
                                f'<h2>{new_comment.text}</h2>')
    return HttpResponse(f'<h1>Метод не разрешен</h1>')


def detail(request, *args, **kwargs):
    post_id = request.objects.GET.get('post_id')
    post = Post.objects.get(Post, pk=post_id)

    return HttpResponse(f'<h1>{post.title}</h1>'
                        f'<p>{post.content}</p>')


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f'<p>{comments.text}</p>')
