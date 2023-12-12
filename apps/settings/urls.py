from django.urls import path
from apps.settings.views import index1,index2, index3

urlpatterns = [
    path('blog-post.html', index1, name = 'index'),
    path('blog.html', index3, name= 'index3'),
    path('', index2, name='index2')
]
