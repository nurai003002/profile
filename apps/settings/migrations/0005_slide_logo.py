# Generated by Django 5.0 on 2023-12-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_remove_slide_description_remove_slide_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='logo',
            field=models.ImageField(default=1, upload_to='Логотип'),
            preserve_default=False,
        ),
    ]
