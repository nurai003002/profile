# from django.shortcuts import render
# from apps.settings.models import Slide
# # Create your views here.
# # def index1(request):
# #     return render(request, 'blog-post.html', locals())
# def index(request):
#     slide = Slide.objects.latest('id')
#     return render(request, 'index-slideshow.html', locals())

# def blog(request):
#     return render(request, 'blog.html', locals())

from django.shortcuts import render
from apps.settings.models import Settings, Slide, AboutUs, Managers, SocialMedia,Customs
# Create your views here.
def index(request):
    customs = Customs.objects.all()
    socia = SocialMedia.objects.latest('id')
    manage = Managers.objects.latest('id')
    settings = Settings.objects.all()
    about = AboutUs.objects.latest('id')
    slide = Slide.objects.latest('id')
    return render(request, 'index-slideshow.html', locals())

def blog(request):
    return render(request, 'blog.html', locals())