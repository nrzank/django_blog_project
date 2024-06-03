
from django.urls import path

from . import views



urlpatterns = [
    # path('', views.index,
    #      name='posts'),
    path('', views.PostView.as_view(),
         name='posts'),
    path('<int:post_id>/',
         views.detail,
         name='post-detail'),
    path('comments/', views.comment,
         name='comments'),
    path('create_post/',
         views.create_post,
         name='create-post'),
    path('create_comment/',
         views.create_comment,
         name='create-comment'),

]
