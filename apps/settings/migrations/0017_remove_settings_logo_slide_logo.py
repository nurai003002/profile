# Generated by Django 5.0 on 2023-12-14 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0016_delete_aboutus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='logo',
        ),
        migrations.AddField(
            model_name='slide',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/', verbose_name='Логотип'),
            preserve_default=False,
        ),
    ]
