# Generated by Django 5.0 on 2023-12-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0022_rename_manager_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('skype', models.URLField(verbose_name='Skype')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('linkedin', models.URLField(verbose_name='Linkedin')),
                ('youtube', models.URLField(verbose_name='Youtube')),
            ],
        ),
    ]
