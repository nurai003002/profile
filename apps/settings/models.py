from django.db import models

# Create your models here.
class Slide(models.Model):
    we_name = models.CharField(
        max_length=255,
        verbose_name="Название salimo"

    )
    mini_descriptions = models.CharField(
        max_length=255,
        verbose_name="Мини Описание для salimo"
    )
    image = models.ImageField(
        upload_to="main_photo",
        verbose_name='Главное фото'
    )
    we_creative = models.CharField(
        max_length=255,
        verbose_name="Название для we creative"
    )
    mini_descriptions1 = models.CharField(
        max_length=255,
        verbose_name="Мини описание для we creative"
    )
    image1 = models.ImageField(
        upload_to="we creative",
        verbose_name="Картина для we creative"
    )
    we_best = models.CharField(
        max_length=255,
        verbose_name="Название для we best"
    )
    mini_descriptions2 = models.CharField(
        max_length=255,
        verbose_name="Мини описание для we best"
    )
    image2 = models.ImageField(
        upload_to=" we best", 
        verbose_name="Картина для we best"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    one_page = models.ImageField(
        upload_to='first_icon',
        verbose_name='Вступление'
    )
    def __str__(self):
        return self.we_name
    
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = "Настройка"

    