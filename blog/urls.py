
from django.urls import path

from . import views



urlpatterns = [
    path('', views.post_get),
    path('<int:post_id>/', views.detail),
    path('comments/', views.comment)

]
