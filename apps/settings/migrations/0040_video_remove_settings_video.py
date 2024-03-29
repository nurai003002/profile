# Generated by Django 5.0 on 2023-12-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0039_delete_video_settings_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(verbose_name='Ютюб видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.RemoveField(
            model_name='settings',
            name='video',
        ),
    ]
