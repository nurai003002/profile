# Generated by Django 5.0 on 2023-12-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0040_video_remove_settings_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Имя')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
    ]
