from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# from django_1.blog.models import Post, Comment
#

# Create your views here.


# def index(request, *args, **kwargs):
#     post = Post.objects.get(pk=1)
#     print(post)
#     return HttpResponse(f"<h1>{post.title} </h1>"
#                         f"<p>{post.content}</p>")
#     context = {
#         'post': post
#     }
#     template = loader.get_template('blog/index.html')
#     return HttpResponse(template.render(context))



# def comment(request, *args, **kwargs):
#     # post_id = request.GET['post_id']
#     # post = Post.objects.get(pk=post_id)
#
#     comments = Comment.objects.get(pk=1)
#
#     return HttpResponse(f"<p>{comments.text}</p>")
#
