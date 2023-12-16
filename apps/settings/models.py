from django.db import models

# Create your models here.
class Settings(models.Model):
    schedule1 = models.CharField(
        max_length = 255,
        verbose_name = 'Расписание'
    )
    schedule2 = models.CharField(
        max_length = 255,
        verbose_name = 'Расписание2'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефон'
    )
    fax = models.CharField(
        max_length = 255,
        verbose_name = 'Факс'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    logo = models.ImageField(
        upload_to='logo',
        verbose_name='Логотип'
    )
    one_page = models.ImageField(
        upload_to='first_icon',
        verbose_name='Вступление'
    )
    def __str__(self):
        return self.schedule1
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = "Настройки"


class Slide(models.Model):
    name = models.CharField(max_length = 255, 
        verbose_name = 'Название'
    )
    descriptions = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='photo',
        verbose_name= 'фото_слайд'
    )
    def __str__(self):
        return self.name
    
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
        return self.descriptions1

    class Meta:
        verbose_name = 'Про меня'
        verbose_name_plural = "Про нас"



class Managers(models.Model):
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
 
    instagram = models.URLField(
        verbose_name = "Instagram",
    )
   
    google = models.URLField(
        verbose_name = 'Google'
    )
     
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджера'


class SocialMedia(models.Model):
    google = models.URLField(
        verbose_name = 'Google'
    )
    facebook = models.URLField(
        verbose_name = 'Facebook'
    )
    instagram = models.URLField(
        verbose_name = 'Instagram'
    )
    youtube = models.URLField(
        verbose_name = 'Youtube'
    )

    def __str__(self):
        return self.instagram
    
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
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = "Отзывы"


class Cards(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Facts(models.Model):
    project = models.CharField(
        max_length = 255, 
        verbose_name = 'Кол-во проектов'
    )
    home_work = models.CharField(
        max_length = 255, 
        verbose_name = 'работа дома'
    )
    office = models.CharField(
        max_length = 255, 
        verbose_name = 'Офис'
    )
    customs = models.CharField(
        max_length = 255, 
        verbose_name = 'Клиенты'
    )

    def __str__(self):
        return self.project
    
    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'


class Team(models.Model):
    image = models.ImageField(
        upload_to='photo',
        verbose_name='Фото'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    instagram = models.URLField(
        verbose_name = "Instagram",

    )
    telegram = models.URLField(
        verbose_name = "telegram"
    )
    google = models.URLField(
        verbose_name = 'Google'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class Post(models.Model):
    image = models.ImageField(
        upload_to='photo',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        verbose_name = 'Описание'

    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True,null = True
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Стятьи'


class Video(models.Model):
    video = models.URLField(
        verbose_name = 'Ютюб видео'
    )
    def __str__(self):
        return 'Видео'
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Portfolio(models.Model):
    image = models.ImageField(
        upload_to='photo',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

class Partner(models.Model):
    image = models.ImageField(
        upload_to='photo',
        verbose_name='Фото'
    )
    def __str__(self):
        return "Партнеры"
    
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


