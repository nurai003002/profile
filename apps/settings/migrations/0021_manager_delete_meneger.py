# Generated by Django 5.0 on 2023-12-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0020_meneger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_photo', models.ImageField(upload_to='manager', verbose_name='Фото менеджера')),
                ('name', models.CharField(max_length=255, verbose_name='Имя менеджера')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.DeleteModel(
            name='Meneger',
        ),
    ]