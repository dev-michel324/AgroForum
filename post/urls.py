from collections import namedtuple
from os import name
from django.http import request
from user.views import index
from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.posts, name='Posts'),
    # path('query', views.posts_search, name='post_search'),
    path('profile', views.profile, name='Profile'),
    path('add_post', views.add_post, name='Add_post'),
    # path('postlist/', views.CategoryListView.as_view(), name='CategoryList'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='CategoryDetailView'),
    path('category/post/<int:id>', views.PostView, name='PostView'),
    path('category/post/postdelete/<int:id>', views.PostDelete, name='PostDelete'),
    path('category/post/commentdelete/<int:id>', views.CommentDelete, name='CommentDelete'),
]