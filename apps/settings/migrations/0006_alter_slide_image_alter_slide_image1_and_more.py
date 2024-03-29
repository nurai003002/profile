# Generated by Django 5.0 on 2023-12-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_slide_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='main_photo', verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image1',
            field=models.ImageField(upload_to='we creative', verbose_name='Картина для we creative'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='logo',
            field=models.ImageField(upload_to='logo/', verbose_name='Логотип'),
        ),
    ]
