from django.urls import path
from apps.settings import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog_news/', views.blog_news, name='blog_news')
]
