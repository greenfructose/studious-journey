# Generated by Django 4.1 on 2022-08-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=250),
        ),
    ]
