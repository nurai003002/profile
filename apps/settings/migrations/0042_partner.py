# Generated by Django 5.0 on 2023-12-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0041_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]