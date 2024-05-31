from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import CommentModelForms
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


def create_post(request, *args, **kwargs):
    print(f'Метод запроса: {request.method}')

    if request.method == 'GET':
        return render(request=request,
                      template_name='blog/create_post.html',
                      )

    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = 1

        if not title or not content:
            return HttpResponse('<h1>Ошибка: Заголовок и содержание обязательны!</h1>', status=400)

        new_post = Post(title=title,
                        content=content,
                        author_id=author_id)
        new_post.save()

        # return redirect(name='post-detail', new_post.pk)
        return HttpResponse(f'<h1>Пост создан!</h1>'
                            f'<h2>{new_post.pk}: {new_post.title}</h2>'
                            f'<h2>{new_post.content}</h2>')

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
            return HttpResponse(f'<h1> Пост создан! </h1>'
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
