# Generated by Django 5.0 on 2023-12-16 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0053_remove_team_facebook_team_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialmedia',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='skype',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='twitter',
        ),
    ]
