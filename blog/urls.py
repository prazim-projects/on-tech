from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('posts/<category>/', views.post_category, name='post_category'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]