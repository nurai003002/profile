# Generated by Django 5.0 on 2023-12-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0051_remove_post_data_remove_post_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='google',
            field=models.URLField(default=1, verbose_name='Google'),
            preserve_default=False,
        ),
    ]