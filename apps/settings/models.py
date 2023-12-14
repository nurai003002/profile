from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    image = models.ImageField(
        upload_to='photo',
        verbose_name= 'фото_слайд'
    )
    descriptions = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = "Настройки"



class Slide(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    one_page = models.ImageField(
        upload_to='first_icon',
        verbose_name='Вступление'
    )
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = "Слайды"



    
class AboutUs(models.Model):
    descriptions1 = models.TextField(
        verbose_name = "Описание1"
    )
    descriptions2 = models.TextField(
        verbose_name = "Описание2"
    )
    descriptions3 = models.TextField(
        verbose_name = "Описание3"
    )
    about_image = models.ImageField(
        upload_to='Photo',
        verbose_name='Фото для About'
    )
    def __str__(self):
        return f"Описание про нас"

    class Meta:
        verbose_name = 'Про меня'
        verbose_name_plural = "Про нас"



class Managers(models.Model):
    # back_image = models.ImageField(
    #     upload_to='back_photo',
    #     verbose_name='Задний image'
    # )
    manager_photo = models.ImageField(
        upload_to='manager',
        verbose_name='Фото менеджера'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя менеджера'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджера'

class SocialMedia(models.Model):
    twitter = models.URLField(
        verbose_name = 'Twitter'
    )
    facebook = models.URLField(
        verbose_name = 'Facebook'
    )
    skype = models.URLField(
        verbose_name = 'Skype'
    )
    instagram = models.URLField(
        verbose_name = 'Instagram'
    )
    linkedin = models.URLField(
        verbose_name = 'Linkedin'
    )
    youtube = models.URLField(
        verbose_name = 'Youtube'
    )

    def __str__(self):
        return f" Соц. сети"
    
    class Meta:
        verbose_name = "Соц.сеть"
        verbose_name_plural = "Соц. сети"


class Customs(models.Model):
    image = models.ImageField(
        upload_to='Image',
        verbose_name='Фото'
    )
    testimonials = models.TextField(
        verbose_name = 'Отзывы'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя клиента"
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Профессия'
    )

    def __str__(self):
        return f"Отзывы"
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"