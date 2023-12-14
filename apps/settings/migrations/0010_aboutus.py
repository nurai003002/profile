# Generated by Django 5.0 on 2023-12-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_remove_slide_logo_black'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Описание')),
                ('about_image', models.ImageField(upload_to='Photo', verbose_name='Фото для About')),
            ],
        ),
    ]
