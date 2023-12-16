
from django.shortcuts import render
from apps.settings import models
# Create your views here.
def index(request):
    partner = models.Partner.objects.all()
    portfolio = models.Portfolio.objects.all()
    youtube = models.Video.objects.latest('id')
    team = models.Team.objects.all()
    facts = models.Facts.objects.last()
    service = models.Cards.objects.all()
    customs = models.Customs.objects.all()
    socia = models.SocialMedia.objects.latest('id')
    manage = models.Managers.objects.latest('id')
    settings = models.Settings.objects.latest('id')
    about = models.AboutUs.objects.latest('id')
    slide = models.Slide.objects.all()
    post = models.Post.objects.all()
    return render(request, 'index-slideshow.html', locals())


def blog_news(request):
    socia = models.SocialMedia.objects.get()
    blog1 = models.Post.objects.all()
    setting = models.Settings.objects.get()
    return render(request, 'blog.html', locals())

def blog_detail(requests, id):
    socia = models.SocialMedia.objects.get()
    setting = models.Settings.objects.get()
    blog = models.Post.objects.get(id=id)
    return render(requests, 'blog-post.html', locals())

