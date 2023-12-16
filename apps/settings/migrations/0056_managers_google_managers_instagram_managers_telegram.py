# Generated by Django 5.0 on 2023-12-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0055_socialmedia_google'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='google',
            field=models.URLField(default=1, verbose_name='Google'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='managers',
            name='instagram',
            field=models.URLField(default=1, verbose_name='Instagram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='managers',
            name='telegram',
            field=models.URLField(default=1, verbose_name='telegram'),
            preserve_default=False,
        ),
    ]
