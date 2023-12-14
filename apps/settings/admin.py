from django.contrib import admin
from apps.settings.models import Settings,Slide, AboutUs, Managers,SocialMedia,Customs
# Register your models here.
admin.site.register(Settings)
admin.site.register(Slide)
admin.site.register(AboutUs)
admin.site.register(Managers)
admin.site.register(SocialMedia)
admin.site.register(Customs)
