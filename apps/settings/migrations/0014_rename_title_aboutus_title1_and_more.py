# Generated by Django 5.0 on 2023-12-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_aboutus_descriptions_aboutus_title_aboutus_title2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='title',
            new_name='title1',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='descriptions',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='descriptions1',
            field=models.TextField(default=1, verbose_name='Описание1 About'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='descriptions2',
            field=models.TextField(default=1, verbose_name='Описание2 About'),
            preserve_default=False,
        ),
    ]
