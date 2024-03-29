# Generated by Django 5.0 on 2023-12-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_remove_settings_logo_slide_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('about_image', models.ImageField(upload_to='Photo', verbose_name='Фото для About')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About us',
            },
        ),
    ]
