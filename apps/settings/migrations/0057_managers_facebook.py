# Generated by Django 5.0 on 2023-12-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0056_managers_google_managers_instagram_managers_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Facebook'),
            preserve_default=False,
        ),
    ]
