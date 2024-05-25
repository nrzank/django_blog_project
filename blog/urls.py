
from django.urls import path

from . import views



urlpatterns = [
    path('', views.post_get),
    path('comments/', views.comment)

]
