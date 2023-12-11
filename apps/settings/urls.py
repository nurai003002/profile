from django.urls import path
from apps.settings.views import index1,index2

urlpatterns = [
    path('1', index1, name = 'index'),
    path('', index2, name='index2')
]