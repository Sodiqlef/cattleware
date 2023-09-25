from django.urls import path
from . import views

urlpatterns = [
    path('blog/list', views.blog_post_list, name='blog_post_list'),
    path('blog/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('blog/create/', views.blog_post_create, name='blog_post_create'),
    path('blog/edit/<int:post_id>/', views.blog_post_edit, name='blog_post_edit'),

]
